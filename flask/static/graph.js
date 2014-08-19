// method to get neighbors for a node
sigma.classes.graph.addMethod('neighbors', function(nodeId) {
    var k,
    neighbors = {},
    index = this.allNeighborsIndex[nodeId] || {};

    for (k in index)
        neighbors[k] = this.nodesIndex[k];

    return neighbors;
});

// these are just some preliminary settings
var g = {
    nodes: [],
    edges: []
};

// Create new Sigma instance in graph-container div (use your div name here) 
s = new sigma({
    graph: g,
    container: 'graph',
    renderer: {
        container: document.getElementById('graph'),
        type: 'canvas'
    },
    settings: {
        minNodeSize: 0.5,
        maxNodeSize: 6.2,
        minEdgeSize: 0.05,
        maxEdgeSize: 5,
        labelThreshold: 6,
        defaultLabelSize: 10,
        defaultEdgeType: 'curvedArrow',
        hideEdgesOnMove: true,
        batchEdgesDrawing: true,
        scalingMode: "outside"
    }
});

/* convert rgb to rgba with a=blah*/
function rgba(c) {
    return c.replace(')', ', 0.75)').replace('rgb', 'rgba');
}



sigma.parsers.gexf(
    'static/trips_gephi.gexf',
    s,
    function(s) {
        // this below adds x, y attributes as well as size = degree of the node 
        var i,
        nodes = s.graph.nodes(),
        edges = s.graph.edges(),
        nodes_len = nodes.length,
        edges_len = edges.length;

        for (i = 0; i < nodes_len; i++) {
            // reverse the y, increase spacing (not sure if that actually works)
            nodes[i].y = nodes[i].y * -20.0;
            nodes[i].x = nodes[i].x * 20.0;

            /* add transparency */
            c = nodes[i]['color'];
            nodes[i]['color'] = rgba(c);
        }

        // change edge type
        for(i = 0; i < edges_len; i++) {
            edges[i].type = "curvedArrow";
        }

        // Refresh the display:
        s.refresh();



        // selecting a node
        s.graph.nodes().forEach(function(n) {
        	  n.originalColor = n.color;
        });
        s.graph.edges().forEach(function(e) {
            e.originalColor = e.color;
        });

        s.bind('clickNode', function(e) {
            var nodeId = e.data.node.id;
            toKeep = s.graph.neighbors(nodeId);
            toKeep[nodeId] = e.data.node;

            s.graph.nodes().forEach(function(n) {
                if (toKeep[n.id])
                    n.color = n.originalColor;
                else
                    n.color = '#979797';
            });

            s.graph.edges().forEach(function(e) {
                if (toKeep[e.source] && toKeep[e.target])
                    e.color = e.originalColor;
                else
                    e.color = '#979797';
            });


            s.refresh();

            updateStationInfo(nodeId);

        });

        s.bind('clickStage', function(e) {
            s.graph.nodes().forEach(function(n) {
                n.color = n.originalColor;
            });

            s.graph.edges().forEach(function(e) {
                e.color = e.originalColor;
            });

            s.refresh();
        });

    }
);
