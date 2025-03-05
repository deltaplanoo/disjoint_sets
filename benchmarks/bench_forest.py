import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random
import time
from structures import disjoint_forest as d
from structures import graph as g
from DAO import dao

def bench(n_list, density):
	print("Benching forest")
	dao.create_database()
	for n in n_list:
		### GENERAL ###
		handler = d.DisjointSetHandler()
		nodes = [d.Node(i) for i in range(n)]
		### GRAPH GENERATION ###
		e = round(density * (n*(n-1))/2)
		graph = g.Graph(nodes)
		graph.generate_edges(e)
		print(f"Graph with {n} nodes and {e} edges -> computed density: {(2*e)/(n*(n-1)):.6f}")

		### FIND CONNECTED COMPONENTS ###
		start = time.perf_counter_ns()
		m = handler.find_connected_components(graph)
		end = time.perf_counter_ns()
		exec_time = (end - start) / 1e9

		print(f"(Forest)   m: {m} - time: {exec_time:.6f} seconds")
		print()

		dao.insert_result("forest", n, m, exec_time)
