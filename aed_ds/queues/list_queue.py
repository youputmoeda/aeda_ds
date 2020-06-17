from .tad_queue import Queue
from ..lists.singly_linked_list import SinglyLinkedList
from ..exceptions import FullQueueException, EmptyQueueException

class ListQueue(Queue):    
    def __init__(self, limit=None):
        self.queue = SinglyLinkedList()
        self.limit = limit

    def is_empty(self): 
        return self.queue.is_empty()

    def is_full(self):
        if not self.limit:
            return False
        return self.limit == self.queue.size()

    def size(self): 
        return self.queue.size()

    def enqueue(self, element):
        if self.is_full():
            raise FullStackException()
        return self.queue.insert_last(element)

    def dequeue(self): 
        if self.is_empty():
            raise EmptyQueueException()
        return self.queue.remove_first()