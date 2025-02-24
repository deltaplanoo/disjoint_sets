class Node:
    def __init__(self, key):
        self.list = None
        self.next = None
        self.key = key
	
    def set_key(self, key):
    	self.key = key

    def set_list(self, list):
        self.list = list

    def set_next(self, next):
        self.next = next
    
    def find_list(self):
        return self.list

class NodeList:
    def __init__(self, node):   # MAKE_SET()
        self.head = None
        self.tail = None
        self.nodes = []
        self.add_node(node)
    
    def add_node(self, node):
        node.set_list(self)
        node.set_next(None)
        if self.head is None:
            self.head = node
        self.nodes.append(node)
        self.tail = node

    def union(self, other_list):
        """
        Union the current list (self) with another list (other_list).
        Attach all members of other_list at the end of the current list.
        """
        if self == other_list:
            return
        self.tail.next = other_list.head
        self.tail = other_list.tail
        self.nodes.extend(other_list.nodes)
        for node in other_list.nodes:
            node.list = self

    def print(self):
        """Print all elements in the set"""
        for node in self.nodes:
            print(node.key, end=" ")
        print()


class DisjointSetHandler:
    def __init__(self):
        # Dictionary to store disjoint sets: {node_key: NodeList}
        self.sets = {}

    def make_set(self, node):
        """Create a new set with a single node."""
        if node.key in self.sets:
            return self.sets[node.key]
        new_set = NodeList(node)
        self.sets[node.key] = new_set
        return new_set

    def find_set(self, node):
        """Find the set containing the given node."""
        return node.find_list()

    def union(self, list1, list2):
        """Union the sets corresponding to list1 and list2."""
        if list1 == list2:
            return  # Already in the same set, do nothing

        list1.union(list2)  # Merge list2 into list1

        for node in list2.nodes: # Remove list2 from the dictionary
            self.sets.pop(node.key, None)  # Remove node from the map

    def generate_nodes(self, n):
        """Generate a list of Node objects with keys from 0 to n-1."""
        return [self.make_set(i) for i in range(n)]

    def find_connected_components(self, graph):
        nodes = graph.nodes
        edges = graph.edges
        for node in nodes:
            self.make_set(node)

        for edge in edges:
            u, v = edge
            self.union(self.find_set(u), self.find_set(v))
        
    def print(self):
        print("Disjoint Sets:")
        for key, node_list in self.sets.items():
            print(f"Set with root {key}: ", end="")
            current_node = node_list.head
            while current_node:
                print(current_node.key, end=" ")
                current_node = current_node.next
            print()
