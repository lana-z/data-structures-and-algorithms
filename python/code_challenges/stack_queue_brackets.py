from data_structures.queue import Queue
from data_structures.stack import Stack

def multi_bracket_validation(string):
    bracket_stack = Stack()
    bracket_queue = Queue()

    for char in string:
        bracket_queue.enqueue(char)

    # Dictionary to hold the bracket pairs
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    while not bracket_queue.is_empty():
        char = bracket_queue.dequeue()

        if char in bracket_pairs.values():
            bracket_stack.push(char)
        elif char in bracket_pairs:
            if bracket_stack.is_empty() or bracket_stack.pop() != bracket_pairs[char]:
                return False

    return bracket_stack.is_empty()

