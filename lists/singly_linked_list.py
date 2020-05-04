from list import List 
from nodes import SingleListNode
import exceptions

class SinglyLinkedList(List):
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
    def get_first(self,exceptions):
        if self.head == None:
            exceptions.EmptyListException()
        else:
            return self.head.get_element()

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self,exceptions):
        if self.head == None :
            exceptions.EmptyListException()
        else:
            return self.tail.get_element()

    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):

        if position < 0 or position < self.size():
            exceptions.InvalidPositionException()
        else:
            current = self.head
            


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.

    def find(self, element, position):
        while self.head != None or self.tail != None:
            element
        else:
            exceptions.NoSuchElementException()



    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):
        f_node = SingleListNode(element, self.head) 
        self.head = f_node
        if self.num_elements == 0:
            self.tail = f_node

        self.num_elements += 1

        """ self.insert(0, self.element)
        self.num_elements += 1"""
    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):
        l_node = SingleListNode(element, None)
        self.tail = l_node
        if self.num_elements == 0:
            self.head = l_node

        self.num_elements += 1

        """self.insert(len(self),self.element)
        self.num_elements += 1"""
    
    
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
            exceptions.InvalidPositionException()


    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        r_head = SingleListNode(self.head, next)
        self.head = r_head
        if self.head != None or self.tail != None:
            self.remove(self.head)
            self.head = next

        self.num_elements -= 1
        """ if self.head != None:
            self.remove(0) """
    
    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        r_tail = SingleListNode(tail, None)
        if self.head != None or self.tail != None:
            self.remove(tail)
            self.tail = num_elements - 1
        self.num_elements -= 1 



        """ if self.head != None:
            self.remove(len(self)) """

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


    def print_it(self):
        cur_node = self.head
        if self.head:
            print(f'Head: {self.head.get_element()}')
            print(f'Tail: {self.tail.get_element()}')
        while cur_node:
            print(cur_node.get_element())
            cur_node = cur_node.next

# criar a lista:
llist = SinglyLinkedList()

# inserir elementos no inicio da lista:
llist.insert_first('C')
llist.insert_first('A')
llist.insert_first('B')

# inserir elementos no fim da lista:
# llist.insert_last('D')

# inserir elementos numa posição expecífica da lista:
# print(llist.insert('B', 1))

# check size:
print(llist.size())

# get the first element of the list:
# print(llist.get_first())

# get the last element of the list:
# print(llist.get_last())

# get the element of the position of the list:
# print(f'position: {1}, element: {llist.get(1)}')
# print(f'position: {2}, element: {llist.get(2)}')
# print(f'position: {0}, element: {llist.get(0)}')

# find elements in the list:
""" print(llist.find('A'))
print(llist.find('B'))
print(llist.find('C'))
print(llist.find('W'))
 """
# remove the first element of the list:
llist.remove_first()

# remove last element of the list: #ERROR
# llist.remove_last()

# imprimir a lista
llist.print_it()

# Make list empty:
# llist.make_empty()

# check if list is empty:
# print(llist.is_empty())