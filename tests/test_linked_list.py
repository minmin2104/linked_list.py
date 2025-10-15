import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.linked_list = LinkedList()

    def test_get_size(self):
        self.assertIsNotNone(self.linked_list.size())
