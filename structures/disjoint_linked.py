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

    def union(self, node1, node2):
        """Union the sets containing node1 and node2."""
        list1 = self.find_set(node1)
        list2 = self.find_set(node2)
        if list1 == list2:
            return  # Already in the same set, do nothing

        list1.union(list2)  # Merge list2 into list1

        for node in list2.nodes: # Remove list2 from the dictionary
            self.sets.pop(node.key, None)  # Remove node from the map

    def weighted_union(self, node1, node2):
        """Union the smaller set with the larger set."""
        list1 = self.find_set(node1)
        list2 = self.find_set(node2)
        if list1 == list2:
            return  # Already in the same set, do nothing
        
        if len(list2.nodes) <= len(list1.nodes):
            list1.union(list2)  # Merge list2 into list1
            for node in list2.nodes: # Remove list2 from the dictionary
                self.sets.pop(node.key, None)  # Remove node from the map
        else:
            list2.union(list1)
            for node in list1.nodes: # Remove list1 from the dictionary
                self.sets.pop(node.key, None)  # Remove node from the map


    def generate_nodes(self, n):
        """Generate a list of Node objects with keys from 0 to n-1."""
        return [self.make_set(i) for i in range(n)]

    def find_connected_components(self, graph):
        m = 0
        for node in graph.nodes:
            self.make_set(node)
            m += 1

        for edge in graph.edges:
            u, v = edge
            self.union(u, v)
            m += 3  # 2 find_set() and 1 union()
        return m

    def weighted_find_connected_components(self, graph):
        m = 0
        for node in graph.nodes:
            self.make_set(node)
            m += 1

        for edge in graph.edges:
            u, v = edge
            self.weighted_union(u, v)
            m += 3
        return m
    
    def print(self):
        print("Disjoint Sets:")
        for key, node_list in self.sets.items():
            print(f"Set with root {key}: ", end="")
            current_node = node_list.head
            while current_node:
                print(current_node.key, end=" ")
                current_node = current_node.next
            print()
