import pandas as pd
import numpy as np

stations = pd.read_csv('../data/stations_10_12_to_11_13.csv',
                       index_col=0)

trips = pd.read_csv('../data/hubwaydata_10_12_to_11_13.csv',
                    index_col=0,
                    parse_dates=['start_date', 'end_date'])

# sigma.js requres the node IDs to be strings.
stations = stations.set_index(stations.index.map(str))
trips.start_station = trips.start_station.map(str)
trips.end_station = trips.end_station.map(str)

print "trips loaded! Ready to roll!"


def get_station_info(node_id):
    return stations.ix[node_id]
