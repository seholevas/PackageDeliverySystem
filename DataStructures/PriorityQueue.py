# Name: Steven Holevas | ID: 001088230
from DataStructures.Heap import MinHeap


# constructor
# calls the min heap as it's priority queue
class PriorityQueue(MinHeap):
    def __init__(self):
        super(PriorityQueue, self).__init__()

    # inserts the key and value into the priority queue using the heap's insert function
    # WORST CASE TIME COMPLEXITY: O(log|N|) WHERE N IS THE # OF ITEMS
    def insert(self, priority_key, element):
        super(PriorityQueue, self).insert((priority_key, element))

    # removes first item in the heap, removes first item as well
    # WORST CASE TIME COMPLEXITY: O(log|N|) WHERE N IS THE # OF ITEMS
    def poll(self):
        if (len(self.heap) != 0):
            return super(PriorityQueue, self).poll()

    # returns the first item in the heap, does not remove the item
    # WORST CASE TIME COMPLEXITY: O(1) WHERE N IS THE # OF ITEMS

    def peek(self):
        if (len(self.heap) != 0):
            return super(PriorityQueue, self).peek()

    # decreases the key of a specific value in the heap

    # WORST CASE TIME COMPLEXITY: O(log|N|)
    def decrease_key(self, new_key, entry):
        index = 0
        # for all the entries in the heap
        # get the key and value, replace the new key and bubble up at the index
        for entries in self.heap:
            if (entries == entry):
                key, value = entries
                key = new_key
                self.heap[index] = (key, value)
                self.bubble_up_at_index(index)
                break

            index += 1
