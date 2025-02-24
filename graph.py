import random

class Graph:
    def __init__(self, nodes):
        """
        Initialize the graph with a list of Node objects.
        """
        self.nodes = nodes
        self.edges = []

    def generate_edges(self, m):
        """
        Generate an undirected graph with m edges using the given Node objects.
        Ensures no self-loops or duplicate edges.
        """
        edges = set()
        num_nodes = len(self.nodes)

        if m > num_nodes * (num_nodes - 1) // 2:
            raise ValueError("Too many edges requested for the number of nodes.")

        while len(edges) < m:
            u = random.choice(self.nodes)  # Pick a random Node
            v = random.choice(self.nodes)  # Pick another random Node
            
            if u != v:  # No self-loops
                edge = (min(u.key, v.key), max(u.key, v.key))  # Ensure uniqueness
                edges.add(edge)

        self.edges = [(self.nodes[u], self.nodes[v]) for u, v in edges]  # Store actual Node pairs

    def print_graph(self):
        """Print the graph's edges."""
        print("Graph edges:")
        for u, v in self.edges:
            print(f"({u.key} - {v.key})")

