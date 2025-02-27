import random
import disjoint_linked as dl
import graph as g
import time
import dao
"""
### GENERAL ###
n = 500
e = 499
handler = dl.DisjointSetHandler()
nodes = [dl.Node(i) for i in range(n)]  # Create n Nodes with keys 0 to n-1

### GRAPH GENERATION ###
graph = g.Graph(nodes)
graph.generate_edges(e)
graph.print_graph()

### CONNECTED COMPONENTS ###
start = time.time()
handler.find_connected_components(graph)
end = time.time()
handler.print()
print(f"Time taken: {end - start:.6f} seconds")
"""
dao.display_results()