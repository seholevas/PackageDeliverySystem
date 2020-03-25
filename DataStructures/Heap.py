# Name: Steven Holevas
class MinHeap():

    # constructor
    # has a capacity, the number of elements in the heap, and the heap itself
    # the heap itself is an array that acts as a tree
    def __init__(self):
        self.capacity = 10
        self.number_of_elements = 0
        self.heap = []

    # returns the left child's index if given the parent's index
    # WORST CASE TIME COMPLEXITY: O(1)
    def get_left_child_index(self, parent_index):
        return(2 * parent_index + 1)

    # returns the right child's index if given the parent's index
    # WORST CASE TIME COMPLEXITY: O(1)
    def get_right_child_index(self, parent_index):
        return(2 * parent_index + 2)

    # gets the parent's index if given the child's index
    # WORST CASE TIME COMPLEXITY O(1)
    def get_parent_index(self, child_index):
        return int((child_index - 1) / 2)

    # determines if the position in the array has a left child
    # WORST CASE TIME COMPLEXITY: O(1)
    def has_left_child(self, index):
        return (self.get_left_child_index(index) < self.number_of_elements)

    # determines if the  position in the array has a right child
    # WORST CASE TIME COMPLEXITY: O(1)
    def has_right_child(self,index):
        return (self.get_right_child_index(index) < self.number_of_elements)

    # determines if the position in the array has a parent
    # WORST CASE TIME COMPLEXITY: O(1)
    def has_parent(self,index):
        return (self.get_parent_index(index) >= 0)

    # returns the left child value if given the index of the parent
    # WORST CASE TIME COMPLEXITY: O(1)
    def get_left_child(self,index):
        return self.heap[self.get_left_child_index(index)]

    # returns the right child value if given the index of the parent
    # WORST CASE TIME COMPLEXITY: O(1)
    def get_right_child(self,index):
        return self.heap[self.get_right_child_index(index)]

    # returns the parent value if given one of the child's indicies
    # WORST CASE TIME COMPLEXITY: O(1)
    def get_parent(self,index):
        return self.heap[self.get_parent_index(index)]

    # swaps one index with another index
    # WORST CASE TIME COMPLEXITY: O(1)
    def swap(self, index_one, index_two):
        self.heap[index_one], self.heap[index_two] = self.heap[index_two], self.heap[index_one]

    # checks if the array [in tree format] needs to be expanded
    # WORST CASE TIME COMPLEXITY: O(N) WHERE N IS THE # OF ITEMS IN THE HEAP
    # WORST CASE SPACE COMPLEXITY: O(N) WHERE N IS THE # OF ITEMS IN THE HEAP/LIST
    def check_dynamic_capacity(self):
        if(self.number_of_elements == self.capacity):
            self.capacity *= 2
            list_double_amount_of_space = [] * (self.capacity)
            self.heap.extend(list_double_amount_of_space)

    # returns the root node of the array
    # WORST CASE TIME COMPLEXITY: O(1)
    def peek(self):
        if(self.number_of_elements == 0):
            raise ValueError("there is nothing in the heap!")
        return self.heap[0]

    # removes the root value of the tree/ heap and replaces it with the last element in the tree
    # the last element in the tree will then bubble down depending on if it has a bigger
    # value then the other items in the heap
    # returns the old root's value

    # WORST CASE TIME COMPLEXITY: O(log|N|) WHERE N IS THE # OF ITEMS IN HEAP
    def poll(self):
        # if no elements, throw error
        if(self.number_of_elements == 0):
            raise ValueError("Heap is empty!")

        # else grab first element, replace it in heap with last element
        # pop last element spot and bubble down the first element
        # which was replaced by the largest element and is rarely also the
        # lowest element.
        else:
            element = self.heap[0]
            self.heap[0] = self.heap[self.number_of_elements - 1]
            self.heap.pop(self.number_of_elements - 1)
            self.number_of_elements -= 1

            self.bubble_down()

        return element

    # this function swaps the parent with the child if the value of the parent is larger than the child's value


    # WORST CASE TIME COMPLEXITY: O(log|N|) WHERE N IS THE # OF ITEMS
    def bubble_down(self):
        index = 0
        # while it has a left child
        while(self.has_left_child(index)):
            index_of_smaller_child = self.get_left_child_index(index)
            # if it has a right child and the right child is smaller than the left child, get the index of the
            # smaller child
            if(self.has_right_child(index) and self.get_right_child(index)[0] < self.get_left_child(index)[0]):
                index_of_smaller_child = self.get_right_child_index(index)
            # if the current item is smaller than the larger item [child], break
            if(self.heap[index][0] < self.heap[index_of_smaller_child][0]):
                break
            # else swap and assign index to smaller child's index [original element]
            # bubbles down
            else:
                self.swap(index, index_of_smaller_child)
            index = index_of_smaller_child

    # this function swaps the child's value with the parent's value if the child's value is smaller than the
    # parent's value
    # WORST CASE TIME COMPLEXITY: O(log|N|) WHERE N IS THE # OF ITEMS
    def bubble_up(self):
        index = self.number_of_elements - 1
        while(self.has_parent(index) and self.heap[index][0] < self.get_parent(index)[0]):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    # inserts an elemeent into the heap, will then perform the function bubble_up() to put new item in the right spot
    # WORST CASE TIME COMPLEXITY: O(log|N|) WHERE N IS THE # OF ITEMS
    def insert(self, element):
        self.check_dynamic_capacity()
        self.heap.append(element)
        self.number_of_elements +=1
        self.bubble_up()

    # returns the number of elements in the array/ tree / heap
    def get_number_of_elements(self):
        return self.number_of_elements

    # returns a boolean that tells whether the array / tree / heap is empty or not
    # WORST CASE TIME COMPLEXITY: O(1) WHERE N IS THE # OF ITEMS
    def is_empty(self):
        return (self.get_number_of_elements() == 0)
