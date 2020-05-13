import unittest

from aed_ds.lists.doubly_linked_list import DoublyLinkedList
from aed_ds.tad_iterator import TwoWayIterator
from aed_ds.exceptions import *

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = DoublyLinkedList()

    # def test_get_previous(self): pass

    # def test_set_previous(self): pass

    # def test_insert_first(self): pass

    # def test_insert_last(self): pass

    # def test_insert(self): pass

    # def test_remove_first(self): pass

    # def test_remove_last(self): pass

    # def test_remove(self): pass

    def test_iterator(self):
        self.assertIsInstance(self.list.iterator(), TwoWayIterator)