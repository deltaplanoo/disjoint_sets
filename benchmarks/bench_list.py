import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import random
import time
from structures import disjoint_linked as d
from structures import graph as g
from DAO import dao

def bench(n_list, density):
	print("Benching linked list")
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
		# Normal & Weighted computed on the same graph
		start = time.perf_counter_ns()
		m = handler.find_connected_components(graph)
		end = time.perf_counter_ns()
		weighted_start = time.perf_counter_ns()
		weighted_m = handler.weighted_find_connected_components(graph)
		weighted_end = time.perf_counter_ns()
		exec_time = (end - start) / 1e9
		weighted_exec_time = (weighted_end - weighted_start) / 1e9
		print(f"(Normal)   m: {m} - time: {exec_time:.6f} seconds")
		print(f"(weighted) m: {weighted_m} - time : {weighted_exec_time:.6f} seconds")
		print()

		# Benchmark results
		dao.insert_result("linked", n, m, exec_time)
		dao.insert_result("weighted_linked", n, weighted_m, weighted_exec_time)
		
