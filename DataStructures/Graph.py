from DataStructures.SinglyLinkedList import SinglyLinkedList
from DataStructures.HashTable import HashTable
from collections import defaultdict
class Graph():
    def __init__(self):
        self.hash_table_starting_node = HashTable(10)
        self.hash_table_connecting_node = HashTable(10)
        # self.graph = defaultdict(dict)
        # self.adjacency_list = {}
        # self.adjacency_list = []

    def add_edge(self, current_node, adding_node, distance_weight):
        key = self.hash_table_connecting_node.hash(current_node.get_element())
        self.hash_table_connecting_node.add(current_node.get_element())
        self.hash_table_starting_node.add(self.hash_table_connecting_node)
        # self.graph[current_node][adding_node] = distance_weight



        # self.adjacency_list.append(node_set)
        # self.graph[current_node] = self.adjacency_list

    def generate_edges(self):
        self.adjacency_list

    #
    # def has_path_BFS(self, source_node, destination_node):

    #
    # def has_path_BFS(self,source_node, destination_node):
    #     sll_next_to_visit = SinglyLinkedList()
    #     visited = HashTable(5)
    #     element = source_node.get_element()
    #     sll_next_to_visit.add(source_node.get_element())
    #
    #     while(sll_next_to_visit.get_size() != 0):
    #         node = sll_next_to_visit.remove(element)
    #
    #         if(node == destination_node):
    #             return True
    #
    #         if(visited.find(destination_node.get_element())):
    #             continue
    #
    #         visited.add(node.get_element())
    #
    #             for child in node.get_children():
    #                 sll_next_to_visit.add(child)
    #     return False

    # def has_path_BFS(self):

