var drawPoset = function(json, n) {

    json = JSON.parse(json);
    
    var drawDiagram = function(node, str) {
        str = str.split("|");
        for(var i in str)
        {
            for(var j in str[i])
            {
                //~ console.log(i,j);
                num = parseInt(str[i][j]);
                node.append("circle")
                    .style("fill", "white")
                    .attr("r", 0.4)
                    .attr("cx", num - n/2)
                    .attr("cy", i);
            }
        }
    };
    
    var levels = [];
    var nodesPerLevel = [];
    for (var i in json.nodes) {
        levels[json.nodes[i].level] = levels[json.nodes[i].level] ? (levels[json.nodes[i].level] + 1) : 1;
        if (nodesPerLevel[json.nodes[i].level] === undefined)
            nodesPerLevel[json.nodes[i].level] = [];
        nodesPerLevel[json.nodes[i].level].push(json.nodes[i]);
    }
    
    var maxLevel = Math.max.apply(null, levels);

    //~ var width = window.innerWidth-15,
    var width = Math.max(window.innerWidth-15, maxLevel*50+50),
        height = n*100+100;

    console.log(json);

    var svg = d3.select("#poset").append("svg")
        .attr("width", width)
        .attr("height", height);

    var link = svg.selectAll(".link")
        .data(json.links)
        .enter().append("line")
        .attr("class", "link");
    
    
    var node = svg.selectAll(".node");
    

    for (var i in nodesPerLevel) {
        node.data(nodesPerLevel[i])
            .enter().append("g")
            .attr("class", "node")
            .attr("transform", function(d, i) {
                return "translate(" + (((maxLevel*50+50)/(levels[d.level] + 1)* ++i)) + "," + ((((levels.length - 1) - d.level) * 100) + 50) + ")";
            })
            .append("circle")
            .attr("class", "node")
            .attr("r", 7);
    }

    svg.selectAll("g").append("text")
        .attr("dx", "0")
        .attr("dy", "25")
        .text(function(d) {
            return d.name
        });
    
    svg.selectAll("g").each(function(d, i) {
        drawDiagram(d3.select(this), d.name);
        var transform = d3.select(this).attr("transform");
        
        var tmp = transform.split(/\(|\)/);
        coord = tmp[1].split(",");
        //~ console.log(tmp);
        //~ console.log(d.name);

        var pos = json.nodes.indexOf(d);
        //~ console.log(json.nodes);
        json.nodes[pos].x = coord[0];
        json.nodes[pos].y = coord[1];
    });
    
    svg.selectAll("g").on("click", function(d) {
        this.parentNode.appendChild(this);
        var dia = d3.select(this)
        if(!dia.attr("big")) {
            dia.attr("big", "set")
                .transition()
                .duration(750)
                .attr("transform", "translate("+ window.innerWidth/2 +","+ window.innerHeight/3 +")scale(23)");
        }
        else {
            dia.attr("big", null)
                .transition()
                .duration(400)
                .attr("transform", function(d) {
                    return "translate(" + json.nodes[json.nodes.indexOf(d)].x + "," + json.nodes[json.nodes.indexOf(d)].y + ")";
                });
        }
    });
    
    link.attr("x1", function(d) { return json.nodes[d.source].x; })
        .attr("y1", function(d) { return json.nodes[d.source].y; })
        .attr("x2", function(d) { return json.nodes[d.target].x; })
        .attr("y2", function(d) { return json.nodes[d.target].y; });
};
