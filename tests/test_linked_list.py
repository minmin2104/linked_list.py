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

    def test_index_of(self):
        self.test_insert()
        a = self.ll.index_of(10)
        self.assertEqual(a, 1)
        b = self.ll.index_of(20)
        self.assertEqual(b, 4)
        self.assertEqual(self.ll.size(), 5)

    def test_search(self):
        self.test_insert()
        self.assertTrue(self.ll.search(5))
        self.assertTrue(self.ll.search(15))
        self.assertFalse(self.ll.search(100))

    def test_delete(self):
        self.test_insert()
        a = self.ll.delete(1)
        self.assertEqual(a, 10)
        self.assertEqual(self.ll.size(), 4)
