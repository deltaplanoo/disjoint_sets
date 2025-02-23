class Node:
    def __init__(self, key):            # MAKE_SET()
        self.list = None
        self.next = None
        self.key = key
	
    def set_key(self, key):
    	self.key = key

    def set_list(self, list):
        self.list = list

    def set_next(self, next):
        self.next = next
    
    def find_list(self):        # maybe i should pass the key (not the node itself)
        return self.list

class NodeList:
    def __init__(self, node):
        self.head = node
        self.tail = node
        self.nodes = []  # Initialize with the single node
        self.size = 1

    def set_head(self, head):
        self.head = head

    def set_tail(self, tail):
        self.tail = tail

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
        self.size += other_list.size
        for node in other_list.nodes:
            node.list = self

    def print(self):
        """Print all elements in the set"""
        for node in self.nodes:
            print(node.key, end=" ")
        print()


class DisjointSetHandler:
    def __init__(self):
        self.sets = []  # List to store all NodeList sets
        
    def make_set(self, key):
        """Create a new set with a single node"""
        node = Node(key)
        new_list = NodeList(node)
        node.set_list(new_list)
        new_list.nodes.append(node)
        self.sets.append(new_list)
        return node
    
    def find_set(self, node):
        """Find the set containing the given node"""
        return node.find_list()

    def union(self, i, j):
        """Union the sets at indexes i and j."""
        if i == j:
            raise ValueError("Cannot union the same set with itself.")
        list1 = self.sets[i]
        list2 = self.sets[j]

        list1.union(list2)
        self.sets.pop(j)

    def print(self):
        """Print all sets with their elements"""
        for i in range(len(self.sets)):
            print(f"Set {i}: ")
            self.sets[i].print()
        print("\n")