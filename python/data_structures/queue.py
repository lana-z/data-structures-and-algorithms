from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None



    def enqueue(self, value):
        #adds a new node with that value to the back of the queue with the provided value
        new_node = Node(value)

        #if queue is empty, add new node to the front
        if self.rear is None:
            self.front = new_node
            self.rear = new_node

       #if queue is not empty, add new node to the rear
        else:
            self.rear.next = new_node
            self.rear = new_node



    def dequeue(self):
        #removes the node from the front of the queue, and returns the node’s value.
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")

        #get the value of the front
        dequeue_value = self.front.value

        #move the pointer to its next node
        self.front = self.front.next

        #queue is empty, so need to update rear - edge case
        if self.front is None:
            self.rear = None

        return dequeue_value



    def peek(self):
        if self.front is None:
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.front.value



    def is_empty(self):
        return self.front is None
