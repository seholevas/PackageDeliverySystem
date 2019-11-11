# class BinaryTree():
#     def __init__(self):
#         self.root = Node()
#         self.binary_tree_size = 1
#
#     def get_size(self):
#         return self.binary_tree_size
#
#     def replace_element(self, node, updated_element):
#         return node.set_element(updated_element)
#
#     def is_root_node(self, node):
#         return (node.get_parent() == None)
#
#     def is_internal_node(self, node):
#         return (node.left_child() != None or node.right_child != None)
#
#     def is_left_child(self, node):
#         if(self.is_root_node(node)):
#             return False
#         return (node ==(node.get_parent().get_right_child()))
#
#     def is_right_child
