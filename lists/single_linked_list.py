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
        while node_to_iterate is not None:
            if node_to_iterate.get_element() == element:
              return position
            else:
                node_to_iterate = node_to_iterate.next_node
                position += 1
            return -1
              

    # Inserts the specified element at the first position in the list.
    def insert_first(self, element):                            # O(1)
        node = SingleListNode(element, self.head)
        self.head = node  
        if self.tail is None:
            self.head = self.tail
        self.num_elements += 1 

    # Inserts the specified element at the last position in the list.
    def insert_last(self, element):                         # O(1)
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
    def remove_first(self):
        if not self.head:
            raise Exception('EmptyListException')
        else:
            node_to_remove = self.head
            self.head = node_to_remove.next_node
        self.num_elements -= 1

    # Removes and returns the element at the last position in the list.
    # Throws EmptyListException.
    def remove_last(self):
        try:
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
            print("EmptyListException")
    
    # Removes and returns the element at the specified position in the list.
    # Range of valid positions: 0, ..., size()-1.
    # Throws InvalidPositionException.
    def remove(self, position):
        if not self.head:
            # raise EmptyListException
            pass
        elif position == 0:
            self.remove_first()
        elif position == self.num_elements - 1:
            self.remove_last()
        else:
            prev_node = self.head
            foll_node = self.head
            old_node = self.head
            index = 0
            while prev_node.next_node:
                if index == position - 1:
                    index = 0
                    old_node = prev_node.next_node
                    break
                prev_node = prev_node.next_node
                index += 1

            while foll_node.next_node:
                if index == position + 1:
                    break
                foll_node = foll_node.next_node
                index += 1

            prev_node.set_next(foll_node)
            self.num_elements -= 1
            return old_node.get_element()
    
    # Removes all elements from the list.
    def make_empty(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    # Returns an iterator of the elements in the list (in proper sequence).
    def iterator(self):
        return single_linked_list.iterator(self)

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.element)
            current_node = current_node.next_node

    def display(self):
        print("teste")

# criar a lista:
llist = single_linked_list()
# inserir elementos no inicio da lista:
llist.insert_first('C')
llist.insert_first('A')
# inserir elementos no fim da lista:
llist.insert_last('D')
# inserir elementos numa posição expecífica da lista:
llist.insert('B', 1)
llist.insert('E', 4)
llist.insert('W', 9)
# imprimir a lista
llist.print_list()

# check size:
print(llist.size())

# get the first element of the list:
print(llist.get_first())
# get the last element of the list:
print(llist.get_last())
# get the element of the position of the list:
print(f'position: {1}, element: {llist.get(1)}')
#print(f'position: {2}, element: {llist.get(2)}')
print(f'position: {0}, element: {llist.get(0)}')
#find elements in the list:
print(llist.find('A'))
print(llist.find('B'))
print(llist.find('C'))
print(llist.find('W'))
# imprimir a lista
llist.print_list()
# remove the first element of the list:
print(f'Primiero elemento foi removido: {llist.remove_first()}')
#remove last element of the list:
print(f'Último elemento foi removido: {llist.remove_last()}')

# remove o elemento que está na posicao indicada:
print(f'Elemento removido: {llist.remove(3)}')   
print(f'Elemento removido: {llist.remove(1)}')   

# imprimir a lista
llist.print_list()