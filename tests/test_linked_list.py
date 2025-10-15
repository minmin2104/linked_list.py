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
        print(self.ll)

    def test_insert_last(self):
        self.ll.insert_last(5)
        self.assertEqual(self.ll.last(), 5)
        self.ll.insert_last(8)
        self.assertEqual(self.ll.last(), 8)
        self.ll.insert_last(12)
        self.assertEqual(self.ll.last(), 12)
        self.assertEqual(self.ll.first(), 5)
        self.assertEqual(self.ll.size(), 3)
        print(self.ll)

    def test_insert(self):
        self.ll.insert_last(5)
        self.ll.insert_last(15)
        self.ll.insert_last(25)
        self.assertEqual(self.ll.size(), 3)
        self.ll.insert(1, 10)
        self.assertEqual(self.ll.size(), 4)
        self.ll.insert(4, 20)
        self.assertEqual(self.ll.size(), 5)
        self.assertEqual(self.ll.last(), 20)
        self.ll.insert(0, 1)
        self.assertEqual(self.ll.first(), 1)
        print(self.ll)

    def test_index_of(self):
        self.test_insert()
        a = self.ll.index_of(10)
        self.assertEqual(a, 2)
        b = self.ll.index_of(20)
        self.assertEqual(b, 5)
        self.assertEqual(self.ll.size(), 6)

    def test_search(self):
        self.test_insert()
        self.assertTrue(self.ll.search(5))
        self.assertTrue(self.ll.search(15))
        self.assertFalse(self.ll.search(100))

    def test_delete(self):
        self.test_insert()
        first = self.ll.delete(0)
        self.assertEqual(first, 1)
        self.assertEqual(self.ll.size(), 5)
        print(self.ll)
        third = self.ll.delete(3)
        self.assertEqual(third, 25)
        self.assertEqual(self.ll.last(), 20)
        print(self.ll)
        last = self.ll.delete(3)
        self.assertEqual(last, 20)
        self.assertEqual(self.ll.last(), 15)
        print(self.ll)

    def test_update(self):
        self.test_insert()
        self.ll.update(0, 0)
        self.assertEqual(self.ll.first(), 0)
        print(self.ll)
        self.ll.update(4, 20)
        self.ll.update(5, 25)
        print(self.ll)
        self.assertEqual(self.ll.last(), 25)
