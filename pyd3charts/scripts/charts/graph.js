
d3.select("#chart")
    .graphviz()
    .renderDot(`{{ data|default("", true) }}`);


