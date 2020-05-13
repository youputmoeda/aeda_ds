import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.exceptions import NoSuchElementException

class TestDoublyLinkedListIterator(unittest.TestCase):
    def setUp(self): pass

    def test_has_next(self):
        """ doubly_linked_list = DoublyLinkedList
        it = doubly_linked_list.iterator()
        self.assertFalse(it.has_next())
        doubly_linked_list.insert_last("element 1")
        doubly_linked_list.insert_last("element 2")
        doubly_linked_list.insert_last("element 3")
        self.assertTrue(it.has_next()) """
        

    # def test_next(self): pass

    # def test_rewind(self): pass

    # def test_has_previous(self): pass
    
    # def test_previous(self): pass

    # def test_full_forward(self): pass
