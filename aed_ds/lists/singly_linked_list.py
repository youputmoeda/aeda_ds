from .tad_list import List
from .nodes import SinglyListNode
from .singly_linked_list_iterator import SinglyLinkedListIterator
from ..exceptions import *


class SinglyLinkedList(List):
   
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
   
    # Returns true if the list contains no elements.
    def is_empty(self):
        return self.num_elements == 0

    # Returns the number of elements in the list.
    def size(self):
        return self.num_elements  

    # Returns the first element of the list.
    # Throws EmptyListException.
    def get_first(self):  
        if not self.head:
            raise EmptyListException()
        return self.head.get_element()

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        if not self.tail:
            raise EmptyListException()
        return self.tail.get_element()
    
    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        if not self.head:
            raise EmptyListException()
        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == position:
                return cur_node.get_element()
            cur_node = cur_node.get_next()
            idx += 1
        return cur_node.get_element()

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        cur_node = self.head
        idx = 0
        while cur_node:
            if element == cur_node.get_element():
                return idx
            cur_node = cur_node.get_next()
            idx += 1
        return -1
              
    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):                            # O(1)
        new_node = SinglyListNode(element, self.head)
        if self.tail is None:
            self.tail = new_node
        self.head = new_node  
        self.num_elements += 1 

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):                         # O(1)
        new_node = SinglyListNode(element, None)            # vai me dar o address que eu quero
        if not self.head:                                   # Se a lista estiver vazia, o self.head = elemento
            self.head = new_node
        else: 
            self.tail.set_next(new_node)               # cria-se a posição a seguir ao tail
        self.tail = new_node
        self.num_elements += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        if position < 0 or position > self.size():
            raise InvalidPositionException()
        elif position == 0:
            return self.insert_first(element)
        elif position == self.size:
            return self.insert_last(element)
        prev_node = self.head
        cur_node = self.head
        idx = 0
        while prev_node:
            if position == idx: 
                new_node = SingleListNode(element, cur_node)
                prev_node.set_next(new_node)
                self.num_elements += 1
                break
            prev_node = cur_node
            cur_node = cur_node.get_next()
            idx += 1
           

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if not self.head:
            raise EmptyListException()
        elif self.head == self.tail:
            self.make_empty
        else:
            node_to_remove = self.head
            self.head = node_to_remove.get_next()
            self.num_elements -= 1
            return node_to_remove.get_element()

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if not self.head:
            raise EmptyListException()
        elif self.head == self.tail:
            return self.remove_first()
        elif self.size() == 2:
            self.head.set_next(None)
            old_none = self.head
            self.tail = self.head
            self.num_elements -= 1
            return old_none.get_element()
            # find second last node e fazer com que esse node se torne no último elemento da minha lista
        cur_node = self.head
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        old_none = self.tail
        self.tail = cur_node
        self.tail.set_next(None)
        self.num_elements -= 1
        return old_none.get_element()

    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        if position < 0 or position>=self.size():
            raise InvalidPositionException()
        elif position == 0:
            return self.remove_first()
        elif position == self.size() -= 1:
            return self.remove_last
        cur_node = self.head
        idx = 0
        while cur_node:
            if idx == position:
                prev_node.set_next(cur_node.get_next())
                old_node = cur_node
                cur_node.set_next(None)
                self.number_elements -= 1
                return node_to_remove.get_element()       
            prev_node = cur_node
            cur_node = cur_node.get_next()
            idx += 1
                        
 
    # # Removes all elements from the list.
    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        return SinglyLinkedListIterator(self)



    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.element)
            current_node = current_node.get_next()
            
# criar a lista:
llist = SinglyLinkedList()
#print(llist.get_first())
# inserir elementos no inicio da lista:
llist.insert_first('C')
llist.insert_first('A')
# inserir elementos no fim da lista:
llist.insert_last('D')
# inserir elementos numa posição expecífica da lista:
# llist.insert('B', 1)
# llist.insert('E', 4)
#print(f'position: {1}, element: {llist.get(45)}')
#llist.insert('W', 9)
# imprimir a lista
llist.print_list()
# print('=' * 30)
# check size:
# print(llist.size())
# print('=' * 30)
# iterator
print(llist.iterator())
print(llist.iterator())
# print('=' * 30)
# get the first element of the list:
# print(llist.get_first())
# get the last element of the list:
# print(llist.get_last())
# print('=' * 30)
# get the element of the position of the list:
# print(f'position: {1}, element: {llist.get(45)}')
# print(f'position: {2}, element: {llist.get(2)}')
# print(f'position: {0}, element: {llist.get(0)}')
# print('=' * 30)
#find elements in the list:
# print(llist.find('A'))
# print(llist.find('B'))
# print(llist.find('C'))
# print(llist.find('W'))
# print('=' * 30)
# imprimir a lista
#llist.print_list()
# remove the first element of the list:
# print(f'Primeiro elemento foi removido: {llist.remove_first()}')
#remove last element of the list:
# print(f'Último elemento foi removido: {llist.remove_last()}')
# print('=' * 30)
# Imprimir a lista
# llist.print_list()
# print('=' * 30)

# remove o elemento que está na posicao indicada:
# print(f'Elemento removido: {llist.remove(3)}')   
# print(f'Elemento removido: {llist.remove(1)}')  
# print('=' * 30) 

# imprimir a lista
# llist.print_list()

