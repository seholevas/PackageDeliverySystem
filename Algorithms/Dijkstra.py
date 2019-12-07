# Name: Steven Holevas | ID: 001088230
from DataStructures.PriorityQueue import PriorityQueue

from DataStructures.Graph import WGUPS_Graph
from DataStructures.HashTable import HashTable
from collections import defaultdict


class Dijkstra:
    """this class uses Dijkstra's algorithm to determine the shortest path"""
    # intializes Dijkstra
    def __init__(self):
        self

    # B1: Algorithm PSUEDOCODE V1
    # 1. Visit each vertex in the graph and mark each one as having a weight of infinity and having no parent,
    #    except the source vertex, mark that one as having a weight of 0
    #
    # 2. Insert source vertex into priority queue
    #
    # 3. While priority queue !=  0: remove vertex element
    #
    # 4. For each vertex linked to vertex element, if current distance > candidate distance then
    #    current distance = candidate distance and parent of candidate vertex = current vertex.
    #
    # 5. Repeat from # 3 until all verticies have been assessed or destination vertex has been reached
    #
    # 6. while end vertex != None, add end to path, ends parent = end
    #
    # 7. reverse order of path
    #
    # 8. return path and distance/weight of path

    # B3: SPACE TIME AND BIG-O
    # WORST CASE TIME COMPLEXITY: O(|E| + |V|log|V|)) WHERE E IS THE # OF EDGES AND V IS THE # OF VERTICIES
    # WORST CASE SPACE COMPLEXITY: O(V + E)  WHERE E IS THE # OF EDGES AND V IS THE # OF VERTICIES


    def dijkstra_shortest_path_with_endpoints(self, graph, source, dest):
        """parameters: graph, source_vertex, destination_vertex
           returns: a shortest path list and the total weight to perform path"""
        # creating variables
        q = PriorityQueue()
        parents = defaultdict(set)
        distances = defaultdict(set)
        start_weight = float("inf")

        # for every vertex in the graph set their weight to infinity and
        # previous vertex to None. Unless, it is the source vertex, then
        # the weight is 0, parent is still None
        for i in graph.get_vertex():
            distances[i].add(start_weight)
            parents[i].add(None)
        distances[source].pop()
        distances[source].add(0)

        # add the source vertex to the priority queue
        q.insert(0, source)

        # while the priority queue is not empty
        while not q.is_empty():
            # remove the minimum value in the priority queue
            # it is a tuple: ( weight/distance between vertices, vertex )
            weight, v = q.poll()

            # for each edge that is connected to the current vertex
            for node in graph.get_edge(v):
                # the current calculated distance is the distance of from the source
                # next vertex
                # distance = distances[v].pop()
                # distances[v].add(distance)
                candidate_distance = weight + node.weight
                # to the current vertex, plus the weight of the current vertex to the

                current_distance = distances[node.vertex].pop()
                distances[node.vertex].add(current_distance)






                # if the distance is smaller than the stored distance, update it
                if current_distance > candidate_distance:
                    distance = candidate_distance
                    parents[node.vertex].pop()
                    parents[node.vertex].add(v)

                    distances[node.vertex].pop()
                    distances[node.vertex].add(distance)

                    # insert the neighbor vertex into the priority queue
                    q.insert(distance, node.vertex)

        # declare and initialize variables
        shortest_path = []
        # end of path
        end = dest

        # while the end is not the first previous node
        # (which is none, because the source vertex's previous is None)
        while end is not None:
            # add the current vertex to the path
            shortest_path.append(end)
            # the next current vertex is the previous of this
            # current vertex
            end = parents[end].pop()

        # reverse the list so it is in the correct order
        shortest_path.reverse()
        return shortest_path, distances[dest].pop()

    # B1: Algorithm PSUEDOCODE V2
    # 1. Visit each vertex in the graph and mark each one as having a weight of infinity and having no parent,
    #    except the source vertex, mark that one as having a weight of 0
    #
    # 2. Insert source vertex into priority queue
    #
    # 3. While priority queue !=  0: remove vertex element
    #
    # 4. For each vertex linked to vertex element, if current distance > candidate distance then
    #    current distance = candidate distance and parent of candidate vertex = current vertex.
    #
    # 5. Repeat from # 3 until all verticies have been assessed or destination vertex has been reached
    #
    # 6. while end vertex != None, add end to path, ends parent = end
    #
    # 7. reverse order of path
    #
    # 8. return path and individual distances/weight of path

    # B3: SPACE TIME AND BIG-O
    # TIME COMPLEXITY: O(|E| + |V|log|V|)) WHERE E IS THE # OF EDGES AND V IS THE # OF VERTICIES
    # SPACE COMPLEXITY: O(V + E)  WHERE E IS THE # OF EDGES AND V IS THE # OF VERTICIES

    def dijkstra_shortest_path_with_endpoints_and_seperated_weights(self, graph, source, dest):
        """parameters: graph, source_vertex, destination_vertex
           returns: a shortest path list and the total weight to perform path"""
        # creating variables
        q = PriorityQueue()
        parents = defaultdict(set)
        distances = defaultdict(set)
        start_weight = float("inf")

        # for every vertex in the graph set their weight to infinity and
        # previous vertex to None. Unless, it is the source vertex, then
        # the weight is 0, parent is still None
        for i in graph.get_vertex():
                distances[i].add(start_weight)
                parents[i].add(None)

        distances[source].pop()
        distances[source].add(0)

        # add the source vertex to the priority queue
        q.insert(0, source)

        # while the priority queue is not empty
        while not q.is_empty():
            # remove the minimum value in the priority queue
            # it is a tuple: ( weight/distance between vertices, vertex )
            weight, v = q.poll()

            # for each edge that is connected to the current vertex
            for node in graph.get_edge(v):
                # the current calculated distance is the distance of from the source
                # to the current vertex, plus the weight of the current vertex to the
                # next vertex
                # distance = distances[v].pop()
                # distances[v].add(distance)
                candidate_distance = weight + node.weight

                # pops the current distance, and adds it back in again
                current_distance = distances[node.vertex].pop()
                distances[node.vertex].add(current_distance)

                # if the distance is smaller than the stored distance, update it
                if current_distance > candidate_distance:
                    distance = candidate_distance
                    parents[node.vertex].pop()
                    parents[node.vertex].add(v)

                    distances[node.vertex].pop()
                    distances[node.vertex].add(distance)

                    # insert the neighbor vertex into the priority queue
                    q.insert(distance, node.vertex)

        # declare and initialize variables
        shortest_path = []
        weights = []

        # end of path
        end = dest

        # while the end is not the first previous node
        # (which is none, because the source vertex's previous is None)
        while end is not None:
            not_updated_end = end
            # add the current vertex to the path
            shortest_path.append(end)
            weights.append(distances[end].pop())
            # the next current vertex is the previous of this
            # current vertex
            end = parents[end].pop()




        #subtracts weights from eachother
        for i in range(len(weights)):
            if(weights[i] != 0):
                weights[i] = weights[i] - weights[i+1]

        # reverse the list so it is in the correct order
        shortest_path.reverse()
        weights.reverse()

        return shortest_path, weights