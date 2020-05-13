from ..exceptions import *
from ..tad_iterator import Iterator

class SinglyLinkedListIterator(Iterator):
    def __init__(self, singly_linked_list):
        self.singly_linked_list = singly_linked_list
        self.rewind()
<<<<<<< HEAD
    
    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
=======

    # Returns true iff the iteration has more elements.
>>>>>>> upstream/develop
    def has_next(self):
        return self.current_node != None

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    def next(self):
        if not self.has_next():
<<<<<<< HEAD
            raise NoSuchElementException
=======
            raise NoSuchElementException()
>>>>>>> upstream/develop
        element = self.current_node.get_element()
        self.current_node = self.current_node.get_next()
        return element

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
<<<<<<< HEAD
    def rewind(self): 
        self.current_node = self.singly_linked_list.head
=======
    def rewind(self):
        self.current_node = self.singly_linked_list.head
>>>>>>> upstream/develop
