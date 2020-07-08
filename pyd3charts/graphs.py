from collections.abc import Iterable

class Graph:

    def __init__(self, vertices=None, edges=None, directed=False):
        self.is_directed = directed
        self.vertices = vertices if vertices is not None else []
        self.edges = edges if edges is not None else []

    def add_vertex(self, value, weight=None):
        self.vertices.append([value, weight])
    
    def add_edge(self, first_vertex, second_vertex, weight=None):
        self.edges.append([first_vertex, second_vertex, weight])
        
    def export_to_graphviz(self):
        header = "graph" if not self.is_directed else "digraph"
        body = ';'.join([f'{edge[0]} {"--" if not self.is_directed else "->"} {edge[1]}' + (f' [weight="{edge[1]}"]' if len(edge) > 2 else '') for edge in self.edges])

        return header + "{" + body + "}"