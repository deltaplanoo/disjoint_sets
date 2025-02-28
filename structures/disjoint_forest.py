class Node:
	def __init__(self, key):
		self.parent = None
		self.key = key
	
	def set_key(self, key):
		self.key = key

	def set_parent(self, parent):
		self.parent = parent
	
	def find_set(self):
		if self.parent is self:
			return self
		return self.parent.find_set()
	
	def union(self, other):
		other_root = other.find_set()
		self_root = self.find_set()
		if other_root is self_root:
			return
		other_root.parent = self_root

class DisjointSetHandler:
    def __init__(self):
        self.sets = {}

    def make_set(self, node):
        """Create a new set with a single node."""
        if node.key in self.sets:
            return self.sets[node.key]
        new_set = node
        new_set.parent = new_set
        self.sets[node.key] = new_set
	
    def find_set(self, node):
        return node.find_set()
	
    def union(self, node1, node2):
        node1.union(node2)

    def find_connected_components(self, graph):
        nodes = graph.nodes
        edges = graph.edges
        m = 0
        for node in nodes:
            self.make_set(node)
            m += 1

        for edge in edges:
            u, v = edge
            self.union(u, v)
            m += 3
        return m
