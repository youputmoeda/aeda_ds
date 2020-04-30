from list import List
from nodes import SingleListNode

class single_linked_list(List):
    # Returns true iff the list contains no elements.
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def is_empty(self):
        if self.head is None:
            return True
        return False

    # Returns the number of elements in the list.
    def size(self):
        return self.num_elements  


    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):
        try:
            if not self.head:
                raise Exception
            else:
                return self.head.get_element()
            
        except:
            print('EmptyListException')

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        try:
            if not self.tail:
                raise Exception
            else:
                return self.tail.get_element()
            
        except:
            print('EmptyListException')
    
    
    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        aux = 0
        node_to_iterate = self.head
        if(position < 0 or position > self.size()):
            print('position invalid')
        while aux < position:
            node_to_iterate = node_to_iterate.next_node
            aux += 1
        return node_to_iterate.get_element()

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        position = 0
        node_to_iterate = self.head
        while node_to_iterate:
            if node_to_iterate.get_element() == element:
              return position
            else:
                node_to_iterate = node_to_iterate.next_node
                position += 1
            return -1
              

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        node = SingleListNode(element, self.head)
        self.head = node
        self.num_elements += 1  
        if self.tail is None:
            self.head = self.tail 

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
    def remove_first(self):
        if not self.head:
            raise Exception('EmptyListException')
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next_node

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
"""         try:
            if not self.head:
                raise Exception
            else:
                node_to_iterate = self.head
                node_to_remove = self.tail
                previous_node = None
                while node_to_iterate.next_node:
                    previous_node = node_to_iterate
                    node_to_iterate = node_to_iterate.next_node

                previous_node = self.tail
                return node_to_iterate.get_element()
        except:
            print("EmptyListException")  """
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position): pass
    
    # Removes all elements from the list.
    def make_empty(self): pass

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self): pass

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.element)
            current_node = current_node.next_node

    def display(self):
        print("teste")

llist = single_linked_list()
llist.print_list()


if __name__=='__main__':
    
    print(single_linked_list)