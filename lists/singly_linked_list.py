from list import List
from nodes import SingleListNode

# from ..exceptions import EmptyListException
# from exceptions import EmptyListException
# from exceptions import InvalidPositionException
# from exceptions import NoSuchElementException


class singly_linked_list(List):
    
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
            raise EmptyListException
            # Exceptions.EmptyListException()
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
        elif not self.head:
            # raise EmptyListException
            pass
        else:
            while position > index:
                cur_node = cur_node.next_node
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
            cur_node = cur_node.next_node
            index += 1
        return -1


    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):                                # O(1)
        new_node = SingleListNode(element, self.head)
        # self.head = self.head.next_node
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
            self.tail.next_node = new_node                       # cria-se a posição a seguir ao tail.  
        self.tail = new_node
        self.num_elements += 1


    # Inserts the specified element at the specified position in the list.
    # Range of valid positions: 0, ..., size().
    # If the specified position is 0, insert corresponds to insertFirst.
    # If the specified position is size(), insert corresponds to insertLast.
    # Throws InvalidPositionException.
    def insert(self, element, position): 
        if position < 0 or position > self.size() + 1:
            # raise InvalidPositionException
            pass
        elif position == 0:
            self.insert_first(element)
        elif position == self.num_elements:
            self.insert_last(element)
        else:
            # get adress do next_node_node
            new_node = self.head
            index = 0
            while new_node:
                index += 1 
                if index == position:
                    new_node.next_node = SingleListNode(element, new_node.next_node)
                    self.num_elements += 1
                    break



    # Removes and returns the element at the first position in the list.
    # Throws EmptyListException.
    def remove_first(self):                                         # O(1)
        if not self.head:
            # raise EmptyListException
            pass
        else:
            old_head = self.head
            self.head = self.head.next_node
            self.num_elements -= 1
            return old_head.get_element()


    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):                                          # O(n)
        if not self.head:
            # raise EmptyListException
            pass
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
        if not self.head:
            # raise EmptyListException
            pass
        elif position == 0:
            self.remove_first()
        else:
            node_to_remove = self.head
            previous_node = None
            index = 0
            while node_to_remove:
                if index == position-1:
                    previous_node = node_to_remove
                    node_to_remove = node_to_remove.next_node
                    old_node = node_to_remove
                    previous_node.set_next(node_to_remove.next_node)
                    return old_node.get_element()
                node_to_remove = node_to_remove.next_node
                index += 1         


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
            cur_node = cur_node.next_node




# criar a lista:
llist = singly_linked_list()

# inserir elementos no inicio da lista:
llist.insert_first('C')
llist.insert_first('A')

# inserir elementos no fim da lista:
llist.insert_last('D')

# inserir elementos numa posição expecífica da lista:
llist.insert('B', 1)
llist.insert('E', 4)
llist.insert('W', 9)

# check size:
# print(f'Tamanho: {llist.size()}')

# get the first element of the list:
# print(f'Primeiro elemento: {llist.get_first()}')

# get the last element of the list:
# print(f'Último elemento: {llist.get_last()}')

# imprimir a lista
llist.print_it()

# get the element of the position of the list:
print(f'position: 1, element: {llist.get(1)}')
print(f'position: 2, element: {llist.get(2)}')
print(f'position: 0, element: {llist.get(0)}')

# find elements in the list:
print(f'elemento: A, position: {llist.find("A")}')
print(f'elemento: B, position: {llist.find("B")}')
print(f'elemento: C, position: {llist.find("C")}')
print(f'elemento: W, position: {llist.find("W")}')


# imprimir a lista
llist.print_it()

# remove the first element of the list:
print(f'Primeiro elemento foi removido: {llist.remove_first()}')

# remove last element of the list:
print(f'Último elemento foi removido: {llist.remove_last()}')

# remove o elemento que está na posicao indicada:
print(f'Elemento 0 foi removido: {llist.remove(1)}')   

# imprimir a lista
llist.print_it()

# Make list empty:
llist.make_empty()

# check if list is empty:
print(llist.is_empty())