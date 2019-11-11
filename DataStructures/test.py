# ############################################################ TEST: SinglyLinkedList.py #################################
from DataStructures.Node import Node
from Data.Package import Package
from DataStructures.HashTable import HashTable
from Data.Location import Location
from DataStructures.SinglyLinkedList import SinglyLinkedList
# from Algorithms.PairingHeap import PairingHeap
from DataStructures.Graph import Graph
import csv

#
#
# p1 = Package()
# p1.package_id_number = "1"
#
# p2 = Package()
# p2.package_id_number = "2"
# p3 = Package()
# p3.package_id_number = "3"
# sll = SinglyLinkedList()
# print("size: "+ str(sll.get_size()))
# sll.insert(p1)
# print("head: " + str(sll.__getattribute__("head_node")))
# sll.insert(p2)
# print("head: " + str(sll.__getattribute__("head_node")))
# sll.insert(p3)
# print("head: " + str(sll.__getattribute__("head_node")))
#
# print("size: "+str(sll.get_size()))
#
# print("traversing")
# sll.traverse()
# print("done traversing")
# print("finding: "+str(sll.find(p2)))
#
# print("remove p3: {0}".format(str(sll.remove(p3))))
# print("size after removal: {0}".format(str(sll.get_size())))
# print("remove p2: {0}".format(str(sll.remove(p2))))
# print("size after removal: {0}".format(str(sll.get_size())))
# print("remove p1: {0}".format(str(sll.remove(p1))))
#
# print("size after removal: {0}".format(str(sll.get_size())))
# ##############################################TEST: HASH TABLE #######################################################
#
p1 = Package("sfj",Location(1,1,1,2),"sfj","sfj","sdfh")
p2 = Package("sfj",Location(1,1,1,3),"sfj","sfj","sdfh")
p3 = Package("sfj",Location(1,1,1,5),"sfj","sfj","sdfh")

p1.package_id_number = "1"
p1.delivery_zip_code = 139849

p2.package_id_number = "2"
p2.delivery_zip_code = 139849



p3.package_id_number = "3"
p3.delivery_zip_code= 139849

# ht = HashTable()
# #
# ht.add(p1)
# ht.add(p2)
# ht.add(p3)
# #
# print("find element: " + str(ht.find(p1)))
#
# print("traverse all added")
# ht.traverse()
# print("done traversing")
# print("removed: " + ht.remove(p3))
#
# print("traversal removed: ")
# ht.traverse()

# print(ht.buckets.__len__())
# print(ht.buckets)
################################################## TESTING: CSV READER AND HASHING #####################################
# ht = HashTable(7)
# package = None
# with open("../CSV/WGUPSPackageFile.csv", 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     for line in csv_reader:
#         # print(Package(line[1]))
#         # print(line ["Starting Place"])
#         package = Package(line["Package ID"], Location(line["Address"], line["City"], line["State"], line["Zip"]),
#                           line["Delivery Deadline"], line["Weight"], line["Special Notes"])
#         ht.add(package)
#         print(str(ht.find(package)) + " In Bucket: " + str(ht.hash(package)))
#         # print(package)
# # ht.traverse()
# print("number of elements: " + str(ht.get_number_of_elements()))
#
# print("NEW LIST")
# new_package = package
# new_package.special_notes = "THIS IS A NEW PACKAGE"
# new_package.package_id_number = 6000003
# ht.update(package, new_package)
# print("traversing")
# ht.traverse()
#
# print("DELETING:" + str(new_package))
# ht.remove(new_package)
# ht.traverse()
#
#
#
# print(ht.get_number_of_elements())

########################################################################################################################

graph = Graph()

# graph = Graph()
node_a = Node(p1)
node_b = Node(p2)
node_c = Node(p3)

graph.add_edge(node_a, node_b, 9)
graph.add_edge(node_b, node_c, 8)
graph.add_edge(node_a, node_c, 10)
graph.add_edge(node_b, node_c, 2)
print(node_a)
print(node_b)
print(node_c)
print(graph.graph)
# j = []
# j.append(node_b)
# j.append(node_c)
# node_a.set_children(j)
# node_b.set_children(node_c)
#
# print(str(graph.has_path_BFS(node_a, node_c)))
# print(str(node_a.get_children()))