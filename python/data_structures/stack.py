from data_structures.linked_list import Node

class Stack:

    def __init__(self):
        self.top = None


    def push(self, value):

        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node


    def pop(self):
        if self.top is None:
            raise ValueError("Stack is empty")

        pop_value = self.top.value
        #move the pointer which "removes" the node
        self.top = self.top.next

        return pop_value


    def peek(self):
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.value


    def is_empty(self):
        return self.top is None
