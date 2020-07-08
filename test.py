from pyd3charts.base import scatter_chart, multiseries_scatter_chart, graph_chart
from pyd3charts.graphs import Graph
from random import randint

## Scatter plot chart with random values without 0 and 100

scatter_chart(
    data = [[randint(0, 100), randint(0, 100)] for _ in range(0, 100)],
    title='TEST CHART',
    header='TEST CHART',
    offset=1,
    top=10,
    right=30,
    bottom=30,
    left=60,
    width=500,
    height=500,
    radius=5,
    fill="red",
    background="gray",
    bodybackground="gray",
    axis=True,
    tooltip=True,
    exportpath='./example.html'
)

# Multi-series scatter plot chart with random values between 0 and 100

multiseries_scatter_chart(
    data = [
        ["serie1", [[randint(0, 100), randint(0, 100)] for _ in range(100)]], 
        ["serie2", [[randint(0, 100), randint(0, 100)] for _ in range(100)]], 
        ["serie3", [[randint(0, 100), randint(0, 100)] for _ in range(100)]]
    ],
    title='TEST CHART',
    header='TEST CHART',
    offset=1,
    top=10,
    right=30,
    bottom=30,
    left=60,
    width=500,
    height=500,
    radius=5,
    fill="red",
    background="gray",
    bodybackground="gray",
    axis=True,
    tooltip=True,
    exportpath='./example.html'
)

## Graphviz example

graph = Graph(
    vertices=['a', 'b', 'c', 'd', 'e', 'f'], 
    edges=[['a', 'b'], ['b', 'c'], ['a', 'c'], ['d', 'c'], ['e', 'c'], ['e', 'a']],
    directed=True
)

graph_chart(graph, exportpath='./example.html')

graph = '''
digraph D {

  A [shape=diamond]
  B [shape=box]
  C [shape=circle]

  A -> B [style=dashed, color=grey]
  A -> C [color="black:invis:black"]
  A -> D [penwidth=5, arrowhead=none]

}
'''
graph_chart(graph, exportpath='./example.html')
