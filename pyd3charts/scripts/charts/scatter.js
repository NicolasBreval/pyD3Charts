var data = {{ data|default([], true) }};

if (data.length > 0) {
    var limits = {
        x: {
            max: Math.max.apply(null, data.map(function(d) { return  d[0]})) + {{ offset|default(10, true) }},
            min: Math.min.apply(null, data.map(function(d) { return  d[0]})) - {{ offset|default(10, true) }}
        },
        y: {
            max: Math.max.apply(null, data.map(function(d) { return  d[1]})) + {{ offset|default(10, true) }},
            min: Math.min.apply(null, data.map(function(d) { return  d[1]})) - {{ offset|default(10, true) }}
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
      .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");

    var x = d3.scaleLinear()
        .domain([limits.x.min, limits.x.max])
        .range([ 0, width ]);

    var y = d3.scaleLinear()
        .domain([limits.y.min, limits.y.max])
        .range([ height, 0]);

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
            .style("opacity", 1)
    }
        
    var mousemove = function(d) {
        tooltip
            .html(`x: ${d[0]}, y: ${d[1]}`)
            .style("left", (d3.mouse(this)[0] + 90) + "px")
            .style("top", (d3.mouse(this)[1]) + "px")
    }
        
    var mouseleave = function(d) {
        tooltip
            .transition()
            .duration(200)
            .style("opacity", 0)
    }
    {% endif %}

    svg.append("g")
        .selectAll("dot")
        .data(data)
        .enter()
        .append("circle")
            .attr("cx", function (d) { return x(d[0]) })
            .attr("cy", function (d) { return y(d[1]) })
            .attr("r", {{ radius|default(5, true) }})
            .style("fill", "{{ fill|default("blue", true) }}")
        {% if tooltip %}
        .on("mouseover", mouseover )
        .on("mousemove", mousemove )
        .on("mouseleave", mouseleave )
        {% endif %}
    
} else {
    $("#chart").append("<h2>Impossible to create chart</h2><h3>Reason: no data</h3>")
}


