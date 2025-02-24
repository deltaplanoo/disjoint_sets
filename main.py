import random
import disjoint_linked as dl
import graph as g

### GENERAL ###
n = 10
e = 8
handler = dl.DisjointSetHandler()
nodes = [dl.Node(i) for i in range(n)]  # Create n Nodes with keys 0 to n-1

### GRAPH GENERATION ###
graph = g.Graph(nodes)
graph.generate_edges(e)  # Generate e edges
graph.print_graph()

### CONNECTED COMPONENTS ###
handler.find_connected_components(graph)
handler.print()
