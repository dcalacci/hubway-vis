from flask import Flask, render_template, request, redirect, url_for, jsonify
from reverse_proxied import ReverseProxied
import hubway_utils
import time
import json

app = Flask(__name__)

def convert_to_epoch(dt):
    return time.mktime(dt.timetuple()) * 1000


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/get_station_info', methods=['GET'])
def station_info():
    station_id = int(request.args.get('nodeid').split('.')[0])
    info = hubway_utils.get_station_info(station_id)
    return jsonify(info)


@app.route('/get_station_timeseries', methods=['GET'])
def station_timeseries():
    station_id = int(request.args.get('nodeid').split('.')[0])
    timeseries = hubway_utils.get_station_timeseries(station_id)
    data = {str(k).split()[0]: v for k, v in dict(timeseries).iteritems()}
    d = sorted([{'date': k, 'numtrips': v} for k, v in data.items()])
    return jsonify({'res': d})


@app.route('/get_top_destinations', methods=['GET'])
def get_top_destinations():
    station_id = int(request.args.get('nodeid').split('.')[0])
    res = hubway_utils.top_destinations(station_id)
    res = [{'label': hubway_utils.stations.ix[k].station, 'value': v} for k, v in res.iteritems()]
    return jsonify({'res': res})


if __name__ == '__main__':
    app.run(debug=True)
