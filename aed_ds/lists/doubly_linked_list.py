from .tad_list import List
from .nodes import DoubleListNode
from ..exceptions import EmptyListException, InvalidPositionException

class DoublyLinkedList(List):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns true iff the list contains no elements.
    def is_empty(self): 
        return self.num_elements == 0

    # Returns the number of elements in the list.
    def size(self): 
        return self.num_elements

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self): pass
        

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self): pass

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position): pass

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element): pass

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element): 
        new_node = DoubleListNode(element, self.head, None)
        if not self.head:
            self.tail = new_node
        self.head = new_node
        num_elements += 1
        

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element): pass

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position): pass

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self): pass

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self): pass
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position): pass
    
    # Removes all elements from the list.
    def make_empty(self): pass

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self): pass


    def print_it(self):
        cur_node = self.head
        idx = 0
        if not self.is_empty():
            print(f'Head: {self.head}')
            print(f'Tail: {self.tail}')
        while cur_node:
            print(cur_node.get_element())
            cur_node = cur_node.get_next()