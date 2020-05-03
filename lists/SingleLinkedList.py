from list import List
from nodes import SingleListNode
# from exceptions import EmptyListException
# from exceptions import InvalidPositionException
# from exceptions import NoSuchElementException


class single_linked_list(List):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
    
    # Returns true iff the list contains no elements.
    def is_empty(self):                                             # O(1)
        if not self.head:
            return True


    # Returns the number of elements in the list.
    def size(self):                                                 # O(1)
        return self.num_elements


    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):                                            # O(1)
        if not self.head:
            # raise EmptyListException
            pass
        else:
            return self.head.get_element()


    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):                                             # O(1)
        if not self.head:
            # raise EmptyListException
            pass
        else:
            return self.tail.get_element()


    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):                                        # O(n)
        index = 0
        cur_node = self.head
        if position < 0 or position > self.size():
            # raise InvalidPositionException
            pass
        else:
            while position > index:
                cur_node = cur_node.next
                index += 1
            return cur_node.get_element()


    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):                                        # O(n)
        cur_node = self.head
        index = 0
        while cur_node:
            if element == cur_node.get_element():
                return index
            cur_node = cur_node.next
            index += 1
        return -1


    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):                                # O(1)
        new_node = SingleListNode(element, self.head)
        # self.head = self.head.next
        if not self.head: # ou seja , se a lista estiver vazia
            self.tail = new_node
        self.head = new_node
        self.num_elements += 1


    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):                                 # O(1)
        new_node = SingleListNode(element, None)            # vai me dar o address que eu quero
        if not self.head:                                   # Se a lista estiver vazia, o self.head = elemento
            self.head = new_node
        else:
            self.tail.next = new_node                       # cria-se a posição a seguir ao tail.  
        self.tail = new_node
        self.num_elements += 1


    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):  
        if position < 0 or position > self.size():
            # raise InvalidPositionException
            pass
        elif element == self.head:
            self.insert_first(element)
        elif element == self.tail:
            self.insert_last(element)
        else:
            index = 0
            node_to_iterate = self.head
            while node_to_iterate:
                number += 1
                if number == position:
                    node_to_iterate.next = SingleListNode(element, node_to_iterate.next)
            self.num_elements += 1


    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):                                         # O(1)
        if not self.head:
            # raise EmptyListException
            pass
        else:
            self.head = self.head.next
            self.num_elements -= 1


    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):                                          # O(n)
        if not self.head:
            # raise EmptyListException
            pass
        else:
            pass
            self.num_elements -= 1
    

    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position): pass
    

    # Removes all elements from the list.
    def make_empty(self):                                           # O(1)
        self.head = None
        self.tail = None
        self.num_elements = 0


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
llist = single_linked_list()

# inserir elementos no inicio da lista:
llist.insert_first('C')
llist.insert_first('A')

# inserir elementos no fim da lista:
llist.insert_last('D')

# inserir elementos numa posição expecífica da lista:
print(llist.insert('B', 1))

# check size:
# print(llist.size())

# get the first element of the list:
# print(llist.get_first())

# get the last element of the list:
print(llist.get_last())

# get the element of the position of the list:
print(f'position: {1}, element: {llist.get(1)}')
print(f'position: {2}, element: {llist.get(2)}')
print(f'position: {0}, element: {llist.get(0)}')

# find elements in the list:
print(llist.find('A'))
print(llist.find('B'))
print(llist.find('C'))
print(llist.find('W'))

# remove the first element of the list:
# llist.remove_first()

# remove last element of the list: #ERROR
# llist.remove_last()

# imprimir a lista
llist.print_it()

# Make list empty:
# llist.make_empty()

# check if list is empty:
# print(llist.is_empty())