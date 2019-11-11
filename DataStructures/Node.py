from Data.Package import Package

class Node():
    """This class represents a single node in the data structure"""
    def __init__(self, element = None):
        self.element = element
        self.children = []

    def __str__(self):
        string = "{}"
        return string.format(self.get_element())


    def get_element(self):
        return self.element

    def get_children(self):
        return self.children

    def nullify(self):
        self.element = None
        self.set_children(None)

    def set_element(self, element):
        self.element = element

    def set_children(self,children):
        self.children = children

    def get_hashable(self):
        return self.get_element().get_hashable()
    # def hello(self):
    #     return (self.element.get_package_id_number())
    #
    # def __str__(self):
    #     return "My String!"