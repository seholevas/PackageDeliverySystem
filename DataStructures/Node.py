class Node():
    """This class represents a single node in the data structure. It has two variables:
            element: the element that is inside the node.
            children: the children of then node."""
    def __init__(self, element = None):
        self.element = element
        self.children = []

    # ToString()
    def __str__(self):
        string = "{}"
        return string.format(self.get_element())

    # gets the element
    def get_element(self):
        return self.element
    # gets the children of this element.
    def get_children(self):
        return self.children

    # nullify's the element for python's automatic garbage collection.
    def nullify(self):
        self.element = None
        self.set_children(None)

    # sets this elements value.
    def set_element(self, element):
        self.element = element

    # sets children equal to the children passed.
    def set_children(self,children):
        self.children = children
    # gets the hashtable of the element.
    def get_hashable(self):
        return self.get_element().get_hashable()