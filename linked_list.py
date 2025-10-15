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
        if self.__head is not None:
            new_node = Node(value)
            new_node.next = self.__head
            self.__head = new_node
            self.__size += 1
        else:
            self.__head = Node(value)
            self.__tail = self.__head
            self.__size += 1

    def insert_last(self, value):
        pass

    def insert(self, index, value):
        pass

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
