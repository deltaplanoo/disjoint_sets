from bench_forest import bench as bench_forest
from bench_list import bench as bench_list

def bench_all(n, e, m_max, p):
	bench_list(n, e, m_max, p)
	bench_forest(n, e, m_max, p)

bench_all(10, 3, 10000000, 5)