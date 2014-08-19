from flask import Flask, render_template, request, redirect, url_for, jsonify
import hubway_utils

app = Flask(__name__)
app.config['SERVER_NAME'] = '127.0.0.1:5001'

@app.route('/')
def root():
    return render_template('index.html')


@app.route('/get_station_info', methods=['GET'])
def station_info():
    station_id = int(request.args.get('nodeid').split('.')[0])
    info = hubway_utils.get_station_info(station_id)
    return info.to_json()


if __name__ == '__main__':
    app.run(debug=True)
