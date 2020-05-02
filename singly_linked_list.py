from list import List 
import exceptions
from list import nodes

class SinglyLinkedList(List):
    def __init__(self):
        self.head = None
        self.tail = None 
        self.next = None
        self.num_elements = 0

    # Returns true iff the list contains no elements.
    def is_empty(self):
        return self.head == None
                  
    # Returns the number of elements in the list.
    def size(self):
        return self.num_elements - 1

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self,exceptions):
        if self.head == None:
            EmptyListException.Throws
        else:
            return self.head

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self,exceptions):
        if self.head == None :
            EmptyListException.Throws
        else:
            return self.tail 

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position): pass
        """ if self.position < 0 or self.num_elements - 1:
            InvalidPositionException.Throws
        else:
            current = self.head
            for _ in position: """


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element): pass

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        self.insert(0, self.element)
        self.num_elements += 1

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        self.insert(len(self),self.element)
        self.num_elements += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if position == 0:
            insert_first(self,element)
        elif position > 0 and position < self.num_elments:
            self.insert(self.position,self.alement)
        elif position == self.num_elements:
            self.insert_last(self,element)
        else:
            InvalidPositionException.Throws

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self, element):
        if self.head != None:
            self.remove(0)
    
    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if self.head != None:
            self.remove(len(self))

    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position): pass

    
    # Removes all elements from the list.
    def make_empty(self):
        while self.num_elements != 0:
            self.remove(0)
            self.num_elements -= 1
            return self.num_elements

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self): pass