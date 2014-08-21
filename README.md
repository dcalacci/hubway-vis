hubway-vis
==========

data visualization(s) of hubway data.

[**Live Here**](http://www.dcalacci.net/dataviz/hubway/)

## data

Contains the original data retrieved from the
[Hubway data visualization challenge](http://hubwaydatachallenge.org)
website.

## notebooks

Has code for the notebooks in which I processed the data and the
html/javascript used to visualize it with sigma.js.

## flask

The flask app that actually runs the site itself.

Contains javascript for d3.js charts, the general frontend, and the
sigma.js network visualization.

### running the app

Run:

```
pip install -r requirements.txt
```

to install the python requirements.

then, run:

```
python hubway_viz.py
```
