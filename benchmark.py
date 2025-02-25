import random
import disjoint_linked as dl
import graph as g
import time
import dao

def bench(p):
	dao.create_database()
	n = 10
	e = 2
	while (n <= 10000000):
		### GENERAL ###
		handler = dl.DisjointSetHandler()
		nodes = [dl.Node(i) for i in range(n)]
		### GRAPH GENERATION ###
		graph = g.Graph(nodes)
		graph.generate_edges(e)

		### FIND CONNECTED COMPONENTS ###
		start = time.time()
		handler.find_connected_components(graph)
		end = time.time()
		exec_time = end - start
		print(f"(n, e): ({n}, {e}) - time: {exec_time:.6f} seconds")

		# Benchmark results
		dao.insert_result("linked", n, e, exec_time)
		
		# next
		n = n*p
		e = e*p

bench(5)
