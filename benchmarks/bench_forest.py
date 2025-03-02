import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random
import time
from structures import disjoint_forest as d
from structures import graph as g
from DAO import dao

def bench(n, density, m_max, p):
	print("Benching forest")
	dao.create_database()
	e = round(density * (n*(n-1))/2)
	m = 0
	while (m <= m_max):
		### GENERAL ###
		handler = d.DisjointSetHandler()
		nodes = [d.Node(i) for i in range(n)]
		### GRAPH GENERATION ###
		graph = g.Graph(nodes)
		graph.generate_edges(e)
		print(f"Graph with {n} nodes and {e} edges -> density: {(2*e)/(n*(n-1)):.6f}")

		### FIND CONNECTED COMPONENTS ###
		start = time.time()
		m = handler.find_connected_components(graph)
		end = time.time()
		exec_time = end - start
		print(f"m: {m} - time: {exec_time:.6f} seconds")
		print()

		# Benchmark results
		dao.insert_result("forest", n, m, exec_time)
		
		# Next benchmark
		n = n * p
		e = round(density * (n*(n-1))/2)
