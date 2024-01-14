class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return "NULL"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class TargetError:
    pass
