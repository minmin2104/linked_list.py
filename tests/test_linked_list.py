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

    def test_insert_last(self):
        self.ll.insert_last(5)
        self.assertEqual(self.ll.last(), 5)
        self.ll.insert_last(8)
        self.assertEqual(self.ll.last(), 8)
        self.ll.insert_last(12)
        self.assertEqual(self.ll.last(), 12)
        self.assertEqual(self.ll.first(), 5)
        self.assertEqual(self.ll.size(), 3)

    def test_insert(self):
        self.ll.insert_last(5)
        self.ll.insert_last(15)
        self.ll.insert_last(25)
        self.assertEqual(self.ll.size(), 3)
        self.ll.insert(1, 10)
        self.assertEqual(self.ll.size(), 4)
        self.ll.insert(4, 20)
        self.assertEqual(self.ll.size(), 5)
        self.assertEqual(self.ll.last(), 25)
