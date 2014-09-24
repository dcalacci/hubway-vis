from flask import Flask, render_template, request, url_for, jsonify
import pandas as pd
import time

app = Flask(__name__)


def convert_to_epoch(dt):
    return time.mktime(dt.timetuple()) * 1000


stations = pd.read_csv(url_for('static',
                               file_name='data/stations_10_12_to_11_13.csv'),
                       index_col=0)


trips = pd.read_csv(url_for('static',
                            file_name='data/hubwaydata_10_12_to_11_13.csv'),
                    index_col=0,
                    parse_dates=['start_date', 'end_date'])


# sigma.js requres the node IDs to be strings.
stations = stations.set_index(stations.index.map(str))
trips.start_station = trips.start_station.map(str)
trips.end_station = trips.end_station.map(str)

print "trips loaded! Ready to roll!"


def get_station_info(node_id):
    return stations.ix[node_id]


def get_station_timeseries(station_id, freq='1d', epoch=True):
    """Returns a timeseries of trip numbers for the given station
        and frequency.
    """
    trips_df = trips[trips.start_station == str(station_id)]
    trips_df = trips_df.groupby(['start_date']).size().fillna(0)
    trips_df = trips_df.resample(freq, how='sum').fillna(0)
    return trips_df


def top_destinations(node_id):
    """ Top 33 percent destinations.
    """
    df = trips[trips.start_station == str(node_id)].groupby('end_station').size()
    df.sort(ascending=False)
    tmp_df = df.map(lambda l: float(l)/sum(df))
    n = 0
    items = []
    # get top 25% of trips & their stations
    for i, row in tmp_df.iteritems():
        if n > 0.25:
            break
        else:
            items.append(i)
            n += row
    return dict(df.ix[items])



@app.route('/')
def root():
    return render_template('index.html')


@app.route('/get_station_info', methods=['GET'])
def station_info():
    station_id = int(request.args.get('nodeid').split('.')[0])
    info = get_station_info(station_id)
    return jsonify(info)


@app.route('/get_station_timeseries', methods=['GET'])
def station_timeseries():
    station_id = int(request.args.get('nodeid').split('.')[0])
    timeseries = get_station_timeseries(station_id)
    data = {str(k).split()[0]: v for k, v in dict(timeseries).iteritems()}
    d = sorted([{'date': k, 'numtrips': v} for k, v in data.items()])
    return jsonify({'res': d})


@app.route('/get_top_destinations', methods=['GET'])
def get_top_destinations():
    station_id = int(request.args.get('nodeid').split('.')[0])
    res = top_destinations(station_id)
    res = [{'label': stations.ix[k].station, 'value': v} for k, v in res.iteritems()]
    return jsonify({'res': res})


if __name__ == '__main__':
    app.run(debug=True)
