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
        self.nodes = []
        self.size = 1
    
    def union(self, list):              # UNION() attach nodeList to the end of the current list
        self.size += list.size
        list.set_head(self.tail)
        self.tail.set_next(list.head)   # self tail -> list head
        self.tail = list.tail
        for node in list.nodes:
            node.set_list(self)

    def set_head(self, head):
        self.head = head
    
    def set_tail(self, tail):
        self.tail = tail



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
    
    def union(self, list1, list2):
        """Union the sets"""
        if (list1 != list2):
            self.sets.remove(list2)     # Remove the second list from our sets since it's being merged
            list1.union(list2)          # Perform the union operation
    
    def print_sets(self):
        """Print all sets in a readable format"""
        sets = self.get_all_sets()
        for i, set_elements in enumerate(sets):
            print(f"Set {i + 1}: {set_elements}")