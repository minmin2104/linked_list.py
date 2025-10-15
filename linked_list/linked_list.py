from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingularLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        nodes = []
        curr_node = self.__head
        while curr_node is not None:
            nodes.append(curr_node.value)
            curr_node = curr_node.next
        return "->".join(map(lambda x: str(x), nodes))

    def insert_first(self, value: Any):
        """
        Insert a node at the first index with a value of `value`.
        Making it the new head of the linked list
        """
        if not self.is_empty():
            new_node = Node(value)
            new_node.next = self.__head
            self.__head = new_node
        else:
            self.__head = Node(value)
            self.__tail = self.__head
        self.__size += 1

    def insert_last(self, value: Any):
        """
        Insert a node at the last index with a value of `value`.
        Making it the new tail of the linked list
        """
        if not self.is_empty():
            new_node = Node(value)
            self.__tail.next = new_node
            self.__tail = new_node
        else:
            self.__tail = Node(value)
            self.__head = self.__tail
        self.__size += 1

    def insert(self, index: int, value: Any):
        """
        Insert node with a value of `value` at a specific index.
        If use on an index equals to the size of the linked list,
        it will be the new tail.
        """
        if index == 0:
            self.insert_first(value)
            return
        if index == self.size():
            self.insert_last(value)
            return
        curr_node = self.__head
        i = 0
        while curr_node is not None and i < index - 1:
            curr_node = curr_node.next
            i += 1
        new_node = Node(value)
        curr_node_next = curr_node.next
        curr_node.next = new_node
        new_node.next = curr_node_next
        self.__size += 1

    def index_of(self, value: Any) -> int:
        """
        Get the index of the first encountered node
        with the value of `value` and return the index
        """
        i = 0
        found = False
        curr_node = self.__head
        while curr_node is not None:
            if curr_node.value == value:
                found = True
                break
            curr_node = curr_node.next
            i += 1

        if not found:
            return -1

        return i

    def first(self):
        """
        Get the value of the head
        """
        return self.__head.value

    def last(self):
        """
        Get the value of the tail
        """
        return self.__tail.value

    def search(self, value: Any) -> bool:
        """
        Return a boolean of True if
        the node with a value of `value`
        found within the linked list
        """
        return self.index_of(value) > -1

    def delete_first(self):
        """
        Delete the first node in the linked list
        """
        if self.is_empty():
            return None

        first_node = self.__head
        self.__head = first_node.next
        self.__size -= 1
        return first_node.value

    def delete(self, index: int):
        """
        Delete the node at a specific index
        in the linked list
        """
        if self.is_empty():
            return None

        if index == 0:
            return self.delete_first()

        curr_node = self.__head
        i = 0
        while curr_node is not None and i < index - 1:
            curr_node = curr_node.next
            i += 1
        node_at_index = curr_node.next
        curr_node.next = node_at_index.next
        if index == self.size() - 1:
            self.__tail = curr_node
        self.__size -= 1
        return node_at_index.value

    def update(self, index: int, value: Any):
        """
        Update the value of the node at index `index`
        with a value of `value`
        """
        if self.is_empty():
            return

        i = 0
        curr_node = self.__head
        while curr_node is not None and i < index:
            curr_node = curr_node.next
            i += 1
        curr_node.value = value

    def is_empty(self) -> bool:
        """
        Return True if the linked list is empty. False otherwise
        """
        return self.__size == 0

    def size(self) -> int:
        """
        Return the size of the linked list
        """
        return self.__size
