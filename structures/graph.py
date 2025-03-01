import random

class Graph:
    def __init__(self, nodes):
        """
        Initialize the graph with a list of Node objects.
        """
        self.nodes = nodes
        self.edges = []

    def generate_edges(self, e):
        """
        Generate an undirected graph with e edges using the given Node objects.
        Ensures no self-loops or duplicate edges.
        """
        edges = set()
        num_nodes = len(self.nodes)

        if e > num_nodes * (num_nodes - 1) // 2:
            raise ValueError("Too many edges requested for the number of nodes.")

        while len(edges) < e:
            u = random.choice(self.nodes)  # Pick 2 random nodes
            v = random.choice(self.nodes)
            
            if u != v:  # No self-loops
                if u.key <= v.key:
                    edge = (u, v)
                else:
                    edge = (v, u)
                edges.add(edge)
        
        self.edges = list(edges)  # Store actual Node pairs
        return self.edges

    def print_graph(self):
        """Print the graph's edges."""
        print("Graph edges:")
        for u, v in self.edges:
            print(f"({u.key} - {v.key})")

