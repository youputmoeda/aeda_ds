class SingleListNode:
    def __init__(self, element, next):
        self.element = element
        self.next = next
    
    def get_element(self):
        return self.element
    
    def get_next(self):
        return self.next
    
    def set_element(self, element):
        self.element = element
    
    def set_next(self, next):
        self.next = next

class DoubleListNode(SingleListNode):
    def __init__(self, element, next, previous):
        SingleListNode.__init__(element, next)
        self.previous = previous
    
    def get_previous(self):
        return self.previous
    
    def set_previous(self, previous):
        self.previous = previous
