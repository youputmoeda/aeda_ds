from list import List
from nodes import SinglyListNode
import singly_linked_list_iterator as slli

import sys
sys.path.append('..')

from exceptions import *


class singly_linked_list(List):
   
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0
   
    # Returns true if the list contains no elements.
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
            EmptyListException()

    # Returns the last element of the list.
    # Throws EmptyListException.
    def get_last(self):
        try:
            if not self.tail:
                raise Exception
            else:
                return self.tail.get_element()
        except:
            EmptyListException()
    
    # Returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    def get(self, position):
        aux = 0
        node_to_iterate = self.head
        try:
            if position < 0 or position > self.size():
                raise Exception
            while aux < position:
                node_to_iterate = node_to_iterate.next_node
                aux += 1
            return node_to_iterate.get_element()
        except:
            InvalidPositionException()

    # Returns the position in the list of the
    # first occurrence of the specified element,
    # or -1 if the specified element does not
    # occur in the list.
    def find(self, element):
        position = 0
        node_to_iterate = self.head
        while node_to_iterate is not None:
            if node_to_iterate.get_element() == element:
                return position
            else:
                node_to_iterate = node_to_iterate.next_node
                position += 1
        return -1
              
    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):                            # O(1)
        node = SinglyListNode(element, self.head)
        self.head = node  
        if self.tail is None:
            self.tail = node
        self.num_elements += 1 

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):                         # O(1)
        new_node = SinglyListNode(element, None)            # vai me dar o address que eu quero
        if not self.head:                                   # Se a lista estiver vazia, o self.head = elemento
            self.head = new_node
        else: 
            self.tail.next_node = new_node                       # cria-se a posição a seguir ao tail.  
        self.tail = new_node
        self.num_elements += 1

    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position):
        try:
            if position < 0 or position > self.size() + 1:
                raise Exception
            elif position == 0:
                self.insert_first(element)
            elif position == self.num_elements:
                self.insert_last(element)
            else:
                #get adress do next_node_node
                new_node = self.head
                index = 0
                while new_node:
                    index += 1 
                    if index == position:
                        new_node.next_node = SinglyListNode(element, new_node.next_node)
                        self.num_elements += 1
                        break
        except:
            InvalidPositionException              

    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):
        if not self.head:
            raise EmptyListException()
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next_node
        self.num_elements -= 1
        return node_to_remove.get_element()

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        if not self.head:
            raise EmptyListException()
        else:
            # find second last node e fazer com que esse node se torne no último elemento da minha lista
            node_second_last = self.head
            while node_second_last.next_node.next_node != None:
                node_second_last = node_second_last.next_node
            old_tail = self.tail
            self.tail = node_second_last
            self.tail.set_next(None)
            self.num_elements -= 1
            return old_tail.get_element()

    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        number = 0
        try:
            if position < 0 or position>=self.size():
                raise Exception
            else:
                node_to_iterate = self.head
                previous_node = None
                while node_to_iterate:
                    if number == position:
                        node_to_remove = node_to_iterate
                        previous_node.set_next(node_to_remove.next_node)
                        self.number_elements -= 1
                        return node_to_remove.get_element()
                    else:
                        previous_node = node_to_iterate
                        node_to_iterate = node_to_iterate.next_node
                        number += 1
        except:
            InvalidPositionException()
 
    # # Removes all elements from the list.
    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        # return singly_linked_list.iterator(self)
        iterator = slli.Iterator(self.head) 
        for _ in range(self.size()):
            return iterator.next()



    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.element)
            current_node = current_node.next_node

    def display(self):
        print("teste")

# criar a lista:
llist = singly_linked_list()
#print(llist.get_first())
# inserir elementos no inicio da lista:
llist.insert_first('C')
llist.insert_first('A')
# inserir elementos no fim da lista:
llist.insert_last('D')
# inserir elementos numa posição expecífica da lista:
llist.insert('B', 1)
llist.insert('E', 4)
#print(f'position: {1}, element: {llist.get(45)}')
#llist.insert('W', 9)
# imprimir a lista
llist.print_list()

# check size:
print(llist.size())
print(llist.iterator())
print(llist.iterator())
print(llist.iterator())
# get the first element of the list:
#print(llist.get_first())
# get the last element of the list:
#print(llist.get_last())
# get the element of the position of the list:
#print(f'position: {1}, element: {llist.get(45)}')
#print(f'position: {2}, element: {llist.get(2)}')
#print(f'position: {0}, element: {llist.get(0)}')
#find elements in the list:
# print(llist.find('A'))
# print(llist.find('B'))
# print(llist.find('C'))
# print(llist.find('W'))
# imprimir a lista
#llist.print_list()
# remove the first element of the list:
#print(f'Primeiro elemento foi removido: {llist.remove_first()}')
#remove last element of the list:
# print(f'Último elemento foi removido: {llist.remove_last()}')
# llist.print_list()

# remove o elemento que está na posicao indicada:
# print(f'Elemento removido: {llist.remove(3)}')   
# print(f'Elemento removido: {llist.remove(1)}')   

# imprimir a lista
#llist.print_list()
#if __name__=='__main__':
