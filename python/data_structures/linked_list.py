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

class TargetError:
    pass
