import random

def generate_graph(n, m):
    """
    generate an undirected graph having n nodes and m edges.
    """
    edges = set()
    while len(edges) < m:
        u = random.randint(0, n - 1)
        v = random.randint(0, n - 1)
        if u != v:	# No self loops
            edges.add((min(u, v), max(u, v)))	# No duplicate edges
    return list(edges)
