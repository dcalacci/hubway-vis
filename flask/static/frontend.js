function updateStationInfo(node_id) {
    $.get("/get_station_info",
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
//                console.log('fading out...');
              });
              $.when(fade).done(function() {
                $('#line-graph-container').fadeToggle(500);
//                console.log('fading in...');
              })
              $('#station-info').show('slide', {direction: 'left'}, 500);
          });
}

function updateTimeSeries(node_id, fade) {
    $.get('/get_station_timeseries',
          {'nodeid': node_id},
          function(data) {
            renderGraph(data['res'], fade);
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
