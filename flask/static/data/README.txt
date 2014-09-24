This file contains metadata for both the Trips and Stations table.

Trips Table Variables:
- id: trip id
- status: trip status; "closed" indicates a trip has terminated
- duration: time of trip in seconds
- start_date: start date of trip with date and time, in EST
- start_station: station id of start station
- end_date: end date of trip with date and time, in EST
- end_station_id: station id of end station
- bike_nr: id of bicycle used
- subscription_type: "Registered" is user with membership; "Casual" is user without membership
- zip_code: zipcode of user (only available for registered users)
- birth_date: birth year of user
- gender: gender of user

Stations Table Variables:

Note on variables id versus terminalName: Hubway-assigned terminal names (see variable terminalName below) correspond to physical stations. If stations move from one year to the next, the terminal name does not change. This may cause confusion if analysts try to compare station data from different years. Therefore, MAPC added a station id (see variable id below) that corresponds to stations' latitude and longitude. If stations move, they receive a new station id, even if their terminal name does not change. In most cases, station movements are small (across a street, or a block down the same street). 

- id: station id assigned by MAPC; corresponds to start_station and end_station_id in trips table
- terminalName: Hubway-assigned station identifier
- name: station name
- install_date: date that station opened for the season
- last_day: date that station closed for the season
- lat: station latitude
- lng: station longitude





