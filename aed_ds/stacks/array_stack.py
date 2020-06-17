from .tad_stack import Stack
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import EmptyStackException, FullStackException

import ctypes

class ArrayStack(Stack):
    def __init__(self,limit=10):
        self.limit = limit
        self.stack = (ctypes.py_object * self.limit)()
        self.num_elements = 0

    # Returns true iff the stack contains no elements.
    def is_empty(self):
        return self.num_elements == 0

    # Returns true iff the stack cannot contain more elements.
    def is_full(self):
        return self.num_elements == self.limit

    # Returns the number of elements in the stack.
    def size(self):
        return self.num_elements

    # Returns the element at the top of the stack.
    # Throws EmptyStackException
    def top(self):
        if self.is_empty():
            raise EmptyStackException()
        idx = self.num_elements - 1
        return self.stack[idx]

    # Inserts the specified element onto the top of the stack.
    # Throws FullStackException
    def push(self, element):
        if self.is_full():
            raise FullStackException()
        idx = self.num_elements
        self.stack[idx] = element
        self.num_elements += 1

    # Removes and returns the element at the top of the stack.
    # Throws EmptyStackException
    def pop(self):
        if self.is_empty():
            raise EmptyStackException()
        idx = self.num_elements - 1
        old = self.stack[idx]
        self.stack[idx] = None
        self.num_elements -= 1
        return old