# Name: Steven Holevas | ID: 001088230

from collections import namedtuple
from collections import defaultdict

# same as tuple, just allows you to name it and its tuple items, which makes
# it visibly maintainable and efficient to get variables
Node = namedtuple('Node', ['vertex', 'weight'])

class WGUPS_Graph:

    # constructor
    def __init__(self):
        # instance variable
        self.verticies_dictionary = defaultdict(set)

    # adds edges to each verticies given
    def add_edge(self, source_vertex, destination_vertex, weight):
        self.verticies_dictionary[source_vertex].add(Node(destination_vertex, weight))
        self.verticies_dictionary[destination_vertex].add(Node(source_vertex, weight))

    # gets edges attached to vertex
    def get_edge(self, the_vertex):
        for edge in self.verticies_dictionary[the_vertex]:
            yield edge

    # gets each verticies
    def get_vertex(self):
        for lists in self.verticies_dictionary.values():
            for node in lists:
                yield node.vertex


######################## ignore this ##########################
# class Graph:
#     """this class creates a graph that is used for Djikstra's. It has an adjacency list"""
#     # constructor
#     def __init__(self):
#         # constructor, adjacency list to keep all the verticies
#         self.adjacency_list = [[] for _ in range(10)]
#
#     # adds edge to graph
#     def add_edge(self, source_vertex, destination_vertex, weight):
#         self.adjacency_list[source_vertex].append((weight, destination_vertex))
#         self.adjacency_list[destination_vertex].append((weight, source_vertex))
#
#     # gets edges within vertex
#     def get_edge(self, the_vertex):
#         for edge in self.adjacency_list[the_vertex]:
#             yield edge
#
#     # gets each vertex
#     def get_vertex(self):
#         for vertex in range(10):
#             yield vertex


