var template = '<div><p id="info"></p>\n<span>Nodes per level:</span><br>\n<ul id="nodeslevel"></ul>\n</div><div id="diagram"></div>';

var nodeGrades = function(json) {
    json.linksPerLevel = []
    for(var i in json.nodes) {
        json.nodes[i].grade = 0;
        for(var k in json.links){
            if(json.links[k].source == i)
                json.nodes[i].grade++;
        }
        if(json.linksPerLevel[json.nodes[i].level] === undefined)
            json.linksPerLevel[json.nodes[i].level] = 0;
        json.linksPerLevel[json.nodes[i].level] += json.nodes[i].grade;
    }
    return json;
};


var drawPoset = function(json, n) {
    
    d3.select("#poset").html(template);

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
    
    var zoom = function() {
      svg.attr("transform", "translate(" + d3.event.translate + ")scale(" + d3.event.scale + ")");
    };
    
    var levels = [];
    var nodesPerLevel = [];
    for (var i in json.nodes) {
        levels[json.nodes[i].level] = levels[json.nodes[i].level] ? (levels[json.nodes[i].level] + 1) : 1;
        if (nodesPerLevel[json.nodes[i].level] === undefined)
            nodesPerLevel[json.nodes[i].level] = [];
        nodesPerLevel[json.nodes[i].level].push(json.nodes[i]);
    }

// ---- output info ------------------------------------------------------
    
    json = nodeGrades(json); // add grade attr to all nodes and calculate linksPerLevel
    var number_word = ['one','two','three','four','five','six','seven','eight'];
    
    var grades = [];
    for (var j in json.nodes){
        if (grades[json.nodes[j].level] === undefined)
            grades[json.nodes[j].level] = [];
        if (grades[json.nodes[j].level].indexOf(json.nodes[j].grade) == -1)
            grades[json.nodes[j].level].push(json.nodes[j].grade ? json.nodes[j].grade : 0);
    }
    
    d3.select("#info").text("The Poset of diagram for the antichain of " + n + " have " + json.nodes.length + " nodes")
    
    var info = d3.select("#nodeslevel");
    levels.reverse();
    grades.reverse();
    json.linksPerLevel.reverse();
    
    info.selectAll('li').data(levels)
        .enter().append("li")
        .text(function(d, i) { 
            var word = (levels[i] == 1) ? 'node' : 'nodes';
            var childList = grades[i].sort(function(a,b){ return a > b; }).join(", ");
            return "Level " + number_word[i] + " has " + d + " " + word + " with " + childList + " children. There's "
            + json.linksPerLevel[i] + " connections to the next level";
        });
        
    levels.reverse();

//---------- draw svg ----------------------------------------------
    var maxLevel = Math.max.apply(null, levels);

    var width = Math.max(window.innerWidth-15, maxLevel*50+50),
        height = n*(width*0.5625)/(n+1)+100;

    //~ console.log(json);

    var svg = d3.select("#diagram").append("svg")
        .attr("width", window.innerWidth-15)
        .attr("height", window.innerHeight-150)
        .append("g")
        .call(d3.behavior.zoom().scaleExtent([-1, 5]).on("zoom", zoom))
        .append("g");

    svg.append("rect")
        .attr("class", "overlay")
        .attr("width", maxLevel*50+50)
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
                return "translate(" + (((maxLevel*50+50)/(levels[d.level] + 1)* ++i)) + "," + ((((levels.length - 1) - d.level) * (width*0.5625)/(n+1)) + 50) + ")";
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
