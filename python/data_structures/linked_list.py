class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def __str__(self):
        result = []
        current = self.head

        string_representation = ""

        while current:
            string_representation += f"{{ {current.value} }} -> "
            current = current.next

        string_representation += "NULL"
        return string_representation

    def includes(self, value):
        current = self.head

        while current:
            if current.value == value:
                return True
            current = current.next

        return False

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            raise TargetError("Cannot insert before in an empty list")

        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if current.next is None:
            raise TargetError("Value not found in the list")

        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node

    def insert_after(self, value, new_value):
        if not self.head:
            raise TargetError("Cannot insert after in an empty list")


        current = self.head

        while current and current.value != value:
            current = current.next

        if current is None:
            raise TargetError("Value not found in the list")

        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node


class TargetError(Exception):
    pass
