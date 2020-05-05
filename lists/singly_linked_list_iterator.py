import sys
sys.path.append('..')

from exceptions import *

class Iterator():
    
    def __init__(self,target):
        self.target = target
        self.first = target


    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an element rather than throwing an exception.
    def has_next(self):
        if self.target.get_next() != None:
            return True
        return False

    # Returns the next element in the iteration.
    # Throws NoSuchElementException
    def next(self):
        try:    
            if self.has_next() is False:
                raise Exception
            else:
                elem = self.target.get_element()
                self.target.get_next()
                return elem     
        except:
            NoSuchElementException()
            

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first element in the iteration.
    def rewind(self):
        self.target = self.first
        self.next()