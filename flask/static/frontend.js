function updateStationInfo(node_id) {
    console.log('updating station info for node id: ' + node_id);
    $.get($SCRIPT_ROOT + '/get_station_info',
          {'nodeid': node_id},
          function(data) {
              console.log(data);
              // change station name

              $('#station-info').hide('slide', {direction: 'left'}, 500,
                                     function() {
                                         $('#station-name').text(data['station']);
                                         $('#station-town').text(data['municipality']);
                                         });
              fade = $.Deferred();
              $('#line-graph-container').fadeToggle(500, function() {
                updateTimeSeries(node_id, fade);
                console.log('fading out...');
              });
              $.when(fade).done(function() {
                $('#line-graph-container').fadeToggle(500);
                console.log('fading in...');
              })
              $('#station-info').show('slide', {direction: 'left'}, 500);

              updatePieChart(node_id);
          });
}

function updateTimeSeries(node_id, fade) {
    $.get($SCRIPT_ROOT + '/get_station_timeseries',
          {'nodeid': node_id},
          function(data) {
	      console.log("updating station timeseries for node: " + node_id);
              renderGraph(data['res'], fade);
          });
}

function getTimeSeries(node_id, fade) {
    $.get($SCRIPT_ROOT + '/get_station_timeseries',
          {'nodeid': node_id},
          function(data) {
            return data;
          });
}

function updatePieChart(node_id) {
  $.get($SCRIPT_ROOT + '/get_top_destinations',
        {'nodeid': node_id},
        function(data) {
          change(data['res']);
        });
}

function updateGraphSize() {
    var graph_height = $(window).height() - $('#graph-container').offset().top;
    $('#graph-container').height(graph_height);
}

$(document).ready(function() {
    updateGraphSize();
});

$(function() {
    $(window).resize(function() {
        updateGraphSize();
    });
    $(window).resize();
});
