import unittest

from linked_list import SingularLinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = SingularLinkedList()

    def test_insert_first(self):
        self.ll.insert_first(5)
        self.assertEqual(self.ll.first(), 5)
        self.ll.insert_first(8)
        self.assertEqual(self.ll.first(), 8)
        self.ll.insert_first(12)
        self.assertEqual(self.ll.first(), 12)
        self.assertEqual(self.ll.last(), 5)
        self.assertEqual(self.ll.size(), 3)
