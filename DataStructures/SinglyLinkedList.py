from DataStructures.Node import Node

class SinglyLinkedList():
    def __init__(self):
        self.head_node = None
        self.size = 0

    def add(self, element):
        new_node = Node(element)
        # new_node.get_children()
        new_node.set_children(self.head_node)
        self.head_node = new_node
        self.size +=1

    def remove(self, element):
        previous_node = None
        current_node = self.head_node
        found = False

        while found is False and current_node:
            if(current_node.get_element() == element):
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_children()

        if(current_node == None):
            return None

        if (previous_node == None):
            self.head_node = current_node.get_children()

        else:
            previous_node.set_children(current_node.get_children())

        # temp_node = current_node
        # current_node.nullify()
        self.size -= 1
        return current_node


    def find(self, element):
        current_node = self.head_node
        while current_node:
            if (current_node.get_element() == element):
                return current_node
            elif(current_node.get_children() != None):
                current_node = current_node.get_children()

        return None

    def update(self, old_element, updated_element):
        node = find(old_element)
        node.set_element(updated_element)
        print("In SinglyLinkedList.update() new value of node: " + str(node))


    def traverse(self):
        current_node = self.head_node
        while current_node:
            print(current_node.get_element())
            current_node = current_node.get_children()

    def get_size(self):
        return self.size