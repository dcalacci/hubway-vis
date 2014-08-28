import pandas as pd
import numpy as np
import seaborn as sns
import pandas_utils

stations = pd.read_csv('../data/stations_10_12_to_11_13.csv', 
                       index_col=0)

trips = pd.read_csv('../data/hubwaydata_10_12_to_11_13.csv',
                    index_col=0,
                    parse_dates=['start_date', 'end_date'])

# sigma.js requres the node IDs to be strings.
stations = stations.set_index(stations.index.map(str))
trips.start_station = trips.start_station.map(str)
trips.end_station = trips.end_station.map(str)


def get_trips_for_date(d):
    start_trips = trips[trips.start_date == d].start_station
    end_trips = trips[trips.end_date == d].end_station
    return (list(start_trips),
            list(end_trips))


start_date = sorted(trips.start_date)[0]
end_date = sorted(trips.end_date)[-1]
timerange = pd.date_range(start_date, end_date, freq='min')


starting_ending = timerange.map(get_trips_for_date)

# separate into two lists
starting, ending = zip(*starting_ending)

res = pd.DataFrame({'date': timerange,
					'starting': starting,
					'ending': ending})

res.to_csv('trip_timeseries.csv')