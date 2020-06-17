from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import FullQueueException, EmptyQueueException
import ctypes

class ArrayQueue(Queue):
    def __init__(self,limit=10):
        self.limit = limit
        self.stack = (ctypes.py_object * self.limit)()
        self.num_elements = 0
        
    def is_empty(self):
        return self.num_elements == 0

    def is_full(self):
        return self.num_elements == self.limit

    def size(self):
        return self.num_elements

    def enqueue(self, element):
        if self.is_full():
            raise FullQueueException()
        idx = self.num_elements
        self.stack[idx] = element
        self.num_elements += 1

    def dequeue(self): 
        if self.is_empty():
            raise EmptyQueueException()
        old = self.stack[0]
        if self.num_elements == 1:
            self.stack = (ctypes.py_object * self.limit)()
            self.num_elements = 0
            return old
        idx = self.num_elements - 1
        self.stack = self.stack[1:idx+1]
        self.num_elements -= 1
        return old