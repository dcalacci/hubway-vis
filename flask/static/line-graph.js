var parseDate = d3.time.format("%Y-%m-%d").parse;


var line = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.numtrips); });

function renderGraph(data, fade) {
    console.log("rendering graph for data: " + data)

  // chart dimensions

  var margin = {top: 10, right: 10, bottom: 25, left: 25},
      height = $('#info-bar').height() - margin.top - margin.bottom;
      width = ($('#info-bar').width() - margin.left - margin.right) * .55;


  var x = d3.time.scale()
    .range([0, width]);

  var y = d3.scale.linear()
    .range([height, 0]);

  var xAxis = d3.svg.axis()
    .scale(x)
    .orient("bottom");

  var yAxis = d3.svg.axis()
    .scale(y)
//    .tickValues(y.domain())
    .orient("left");

  // refresh the graph

  d3.select('#line-graph').remove();

  var svg = d3.select("#line-graph-container").append("svg")
    .attr('id', 'line-graph')
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // actual d3 stuff

  var line = d3.svg.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.numtrips); });


  data.forEach(function(d) {
    d.date = parseDate(d.date);
    d.numtrips = +d.numtrips;
  });

  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain(d3.extent(data, function(d) { return d.numtrips; }));

  svg.append("g")
      .attr("class", "x axis")
      .attr("transform", "translate(0," + height + ")")
      .attr('font-size', '10%')
      .call(xAxis);

  svg.append("g")
      .attr("class", "y axis")
      .attr('font-size', '10%')
      .call(yAxis)
    .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .attr("font-size", '10%')
      .style("text-anchor", "end")
      .text("Trips");

  svg.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);

  fade.resolve();
//  console.log('finished rendering');
}
