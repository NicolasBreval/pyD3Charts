var data = {{ data|default([], true) }};

if (data.length > 0) {
    var limits = {
        x: {
            max: {{ max_x }},
            min: {{ min_x }}
        },
        y: {
            max: {{ max_y }},
            min: {{ min_y }}
        }
    };

    var margin = {
        top: {{ top|default(10, true) }},
        right: {{ right|default(30, true) }},
        bottom: {{ bottom|default(30, true) }},
        left: {{ left|default(60, true) }}
    };
    
    var width = {{ width|default(500, true) }} - margin.left + margin.right;
    var height = {{ height|default(500, true) }} - margin.top + margin.bottom;
    
    var svg = d3.select("#chart")
      .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .style("background", "{{ background|default('white') }}")
      .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");
    
    var allGroup = {{ series }};
    
    
    var color = d3.scaleOrdinal()
        .domain(allGroup)
        .range(d3.schemeSet2);

    var allColors = allGroup.map(function(g) { return color(g); });

    function rgb2hex(rgb){
        var rgbColor = "#";

        for (i in rgb) {
            var hex = Number(rgb[i]).toString(16);

            if (hex.length < 2)
                hex = "0" + hex;
            
                rgbColor += hex;
        }

        return rgbColor;
    }

    var x = d3.scaleLinear()
        .domain([limits.x.min, limits.x.max])
        .range([ 0, width ]);

    var y = d3.scaleLinear()
      .domain([limits.y.min, limits.y.max])
      .range([ height, 0 ]);

    {% if axis %}
    svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

    svg.append("g")
      .call(d3.axisLeft(y));
    {% endif %}

    {% if tooltip %}
    var tooltip = d3.select("#chart")
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid")
        .style("border-width", "1px")
        .style("border-radius", "5px")
        .style("padding", "10px")
    
    var mouseover = function(d) {
        tooltip
            .style("opacity", 1);
    }
        
    var mousemove = function(d) {
        var currentGroup = allGroup[allColors.indexOf(rgb2hex($("circle:hover").parent().css("fill").replace("rgb", "").replace("(", "").replace(")", "").split(",")))];
        
        if (currentGroup == undefined) {
            currentGroup = allGroup[allColors.indexOf($("circle:hover").parent().css("fill").replace("rgb", "").replace("(", "").replace(")", "").split(",")[0])]
        }

        tooltip
            .html(`x: ${d[0]}, y: ${d[1]}, group: ${currentGroup}`)
            .style("left", (d3.mouse(this)[0] + 90) + "px")
            .style("top", (d3.mouse(this)[1]) + "px");
    }
        
    var mouseleave = function(d) {
        tooltip
            .transition()
            .duration(200)
            .style("opacity", 0);

        currentSelected = null;
    }
    {% endif %}

    
    svg
        .selectAll(".series")
        .data(data)
        .enter()
            .append('g')
            .attr("name", function(d){ return d.name })
            .style("fill", function(d){ return color(d.name) })
        .selectAll(".series")
        .data(function(d){ return d.values })
        .enter()
            .append("circle")
                .attr("cx", function(d) { return x(d[0]) } )
                .attr("cy", function(d) { return y(d[1]) } )
                .attr("r", 5)
                {% if tooltip %}
                .on("mouseover", mouseover )
                .on("mousemove", mousemove )
                .on("mouseleave", mouseleave )
                {% endif %}
    
    

} else {
    $("#chart").append("<h2>Impossible to create chart</h2><h3>Reason: no data</h3>")
}


