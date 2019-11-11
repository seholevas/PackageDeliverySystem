from DataStructures.Node import Node
class PairingHeap():

    # def __init__(self, root_element = None):
    #     self.root = None
    #
    # def find_min(self):
    #     if self.root is None:
    #         raise ValueError("Heap is empty!")
    #     else:
    #         return self.root.val
    #
    # def _merge(self, root1, root2):
    #     if root1 is None:
    #         return root2
    #     elif root2 is None:
    #         return root1
    #     elif root1.val < root2.val:
    #         root1.children.append(root2)
    #         return root1
    #     else:
    #         root2.children.append(root1)
    #         return root2
    #
    # def insert(self, val):
    #     self.root = self._merge(self.root, Node(val))
    #
    # def delete_min(self):
    #     if self.root is None:
    #         raise ValueError("Heap is empty!")
    #     else:
    #         self.root = self._merge_pairs(self.root.children)
    #
    # def _merge_pairs(self, l):
    #     if len(l) == 0:
    #         return None
    #     elif len(l) == 1:
    #         return l[0]
    #     else:
    #         return self._merge(self._merge(l[0], l[1]), self._merge_pairs(l[2:]))

    # def find_minimum(self):
    #     if(self.root_node != None):
    #         return self.root_node
    #     else:
    #         raise ValueError("Exception in PairingHeap.py | PairingHeap() | PairingHeap.find_minimum(): Heap is empty!")
    #
    # def insert(self, element):
    #     self.root_node = self.meld(self.root_node, Node(element))
    #
    # def merge(self, root_one, root_two):
    #     self
    #
    # def decrease_key(self):
    #     self
    #
    # def delete_minimum(self):
    #     if(self.root_node == None):
    #         raise ValueError("Exception in PairingHeap.py | PairingHeap() | PairingHeap.delete_minimum(): Heap is empty!")
    #     else:
    #         self.root_node = self.merge_pairs(self.root_node.get_children())
    #
    # def meld(self, first_heap, second_heap):
    #     if(first_heap == None):
    #         return second_heap
    #
    #     elif(second_heap == None):
    #         return first_heap
    #
    #     elif(first_heap.root_node.get_element() < second_heap.root_node.get_element()):
    #         self.root_node = first_heap.root_node
    #         self.root_node.get_children().append(second_heap)
            # return self

    #     else:
    #         self.root_node = second_heap.root_node
    #         self.root_node.get_children().append(first_heap)
    #         # return self
    #     return self
    #
    # def merge_pairs(self, other_heap):
    #     if(len(other_heap) == 0):
    #         return None
    #     elif(len(other_heap) == 1):
    #         return list_of_subtrees[0]
    #     else:
    #         return self.meld(self.meld(list_of_subtrees[0], list_of_subtrees[1]), self.merge_pairs(other_heap[2:]))



    # def create_heap(self):
    #     self
    #
    # def decrease_key(self):
    #     self
    #
    # def delete_min(self):
    #     self
    #
    # def extract_min(self):
    #     self
    #
    # def find_min(self):
    #     self
    #
    # def get_size(self):
    #     self
    #
    # def heapify(self):
    #     self
    #
    # def is_empty(self):
    #     self
    #
    # def increase_key(self):
    #     self
    #
    # def meld(self):
    #     self
    #
    # def merge(self):
    #     self
    #
    # def replace(self):
    #     self
    #
    # def sift_up(self):
    #     self
    #
    # def sift_down(self):
    #     self
class Heap():
    def __init__(self):
        self.insertion_node = None
        self.last_node = None

    def insert(self, element):
        self.insertion_node = Node(element)
        self.last_node = self.insertion_node

    def remove(self, element):

