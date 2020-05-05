import sys
sys.path.append('..')
from tad_iterator import *
from exceptions import *

class Iterator():
    
    def __init__(self, maxi):
        self.maxi = maxi
        self.first = maxi


    # Returns true iff the iteration has more elements.
    # In other words, returns true next would return an maxi rather than throwing an exception.
    def has_next(self):
        if self.maxi.get_next() != None:
            return True
        return False
    
    def __iter__(self):
        return self

    # Returns the next maxi in the iteration.
    # Throws NoSuchElementException
    def next(self):
        try:    
            if self.has_next() is None:
                raise Exception
            else: 
                elem = self.maxi.get_element()
                self.maxi = self.maxi.get_next()
                return elem
        except:
            NoSuchElementException()
            

    # Restarts the iteration. After rewind, if the iteration is not empty, next will return the first maxi in the iteration.
    def rewind(self):
        self.maxi = self.first
    