class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingularLinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def insert_first(self, value):
        if not self.is_empty():
            new_node = Node(value)
            new_node.next = self.__head
            self.__head = new_node
        else:
            self.__head = Node(value)
            self.__tail = self.__head
        self.__size += 1

    def insert_last(self, value):
        if not self.is_empty():
            new_node = Node(value)
            self.__tail.next = new_node
            self.__tail = new_node
        else:
            self.__tail = Node(value)
            self.__head = self.__tail
        self.__size += 1

    def insert(self, index, value):
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

    def first(self):
        return self.__head.value

    def last(self):
        return self.__tail.value

    def delete():
        pass

    def search():
        pass

    def update():
        pass

    def is_empty(self) -> bool:
        return self.__size == 0

    def size(self):
        return self.__size
