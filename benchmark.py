import random
import disjoint_linked as dl
import graph as g
import time
import dao

def bench(p):
	dao.create_database()
	n = 50000
	e = 15000
	m = 0
	while (m <= 5000000):
		### GENERAL ###
		handler = dl.DisjointSetHandler()
		nodes = [dl.Node(i) for i in range(n)]
		### GRAPH GENERATION ###
		graph = g.Graph(nodes)
		graph.generate_edges(e)

		### FIND CONNECTED COMPONENTS ###
		start = time.time()
		m = handler.find_connected_components(graph)
		end = time.time()
		exec_time = end - start
		print(f"m: {m} - time: {exec_time:.6f} seconds")

		# Benchmark results
		dao.insert_result("linked", n, m, exec_time)
		
		# Next benchmark
		n = n+p
		e = e+p

bench(25000)
