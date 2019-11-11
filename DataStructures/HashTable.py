from Data.Package import Package
from DataStructures.SinglyLinkedList import SinglyLinkedList
from DataStructures.Node import Node
class HashTable():
    """This class is the HashTable class. It is used to hash and store elements."""

    def __init__(self, number_of_buckets):
        self.number_of_buckets = number_of_buckets
        self.buckets = [None] * self.number_of_buckets
        self.number_of_elements = 0

    def chain_add(self, key, element):
        item_in_bucket = self.buckets[key]

        if(isinstance(item_in_bucket, Package)):
            singly_linked_list = SinglyLinkedList()
            singly_linked_list.add(item_in_bucket)
            singly_linked_list.add(element)
            self.buckets[key] = singly_linked_list
        else:
            item_in_bucket.add(element)
            self.buckets[key] = item_in_bucket


    def hash(self, element):
        key = int(element.get_hashable() % self.number_of_buckets)
        return key



    def add(self, element):

        key = self.hash(element)

        if(self.buckets[key] == None):
            # singly_linked_list = SinglyLinkedList()
            # singly_linked_list.add(element)
            # self.buckets[key] = (singly_linked_list)
            self.buckets[key] = element

        else:
            self.chain_add(key, element)


        self.number_of_elements += 1

    def get_number_of_elements(self):
        return self.number_of_elements


    def find(self, element):
        key = self.hash(element)

        if(self.buckets[key] == element): #or self.buckets[key] == None):
            return element
        elif(self.buckets[key] == None):
            return None
        else:
            return self.buckets[key].find(element)

        return None

    def remove (self, element):
        key = self.hash(element)

        if (isinstance(self.buckets[key], SinglyLinkedList)):
            singly_linked_list = self.buckets[key]
            self.number_of_elements -= 1
            return singly_linked_list.remove(element)
        else:
            self.number_of_elements -= 1
            temp_element = self.buckets[key]
            self.buckets[key] = None
            return temp_element


        return None

    def traverse(self):
        for bucket in self.buckets:
            if(isinstance(bucket, SinglyLinkedList)):
                bucket.traverse()
            elif(bucket != None):
                print(bucket)

    def update(self, old_element, updated_element):
        item_needed_to_be_updated = self.find(old_element)

        if(isinstance(item_needed_to_be_updated, Node)):
            item_needed_to_be_updated.set_element(updated_element)

        elif(isinstance(item_needed_to_be_updated, Package)):
            self.remove(old_element)
            self.add(updated_element)

