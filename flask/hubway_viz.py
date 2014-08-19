from flask import Flask, render_template, request, redirect, url_for, jsonify
import hubway_utils
import time
import json

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5001'


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
    data = json.loads(timeseries.to_json(date_format='iso'))
    d = sorted([{'date': str(k.split('T')[0]), 'numtrips': v} for k, v in data.items()])
    return jsonify({'res': d})


if __name__ == '__main__':
    app.run(debug=True)
