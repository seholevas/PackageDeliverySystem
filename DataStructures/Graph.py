# Name: Steven Holevas

from collections import namedtuple
from collections import defaultdict

# same as tuple, just allows you to name it and its tuple items, which makes
# it visibly maintainable and efficient to get variables
Node = namedtuple('Node', ['vertex', 'weight'])

class WGUPS_Graph:
    """this class is a fully-connected graph. Each node in the graph is connected to every other node. This class has one variable:
            verticies_dictionary: a default dictionary that contains a set. The reason for a set is because it doesn't
            allow for duplicate values. Meaning, There can't be outdated information about one part of the graph."""

    # constructor
    def __init__(self):
        # instance variable
        self.verticies_dictionary = defaultdict(set)

    # adds edges to each vertices given
    def add_edge(self, source_vertex, destination_vertex, weight):
        self.verticies_dictionary[source_vertex].add(Node(destination_vertex, weight))
        self.verticies_dictionary[destination_vertex].add(Node(source_vertex, weight))

    # gets edges attached to vertex
    def get_edge(self, the_vertex):
        for edge in self.verticies_dictionary[the_vertex]:
            yield edge

    # gets each vertices
    def get_vertex(self):
        for lists in self.verticies_dictionary.values():
            for node in lists:
                yield node.vertex

