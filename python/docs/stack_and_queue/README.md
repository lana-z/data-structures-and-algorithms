# Stacks and Queues
This project is to use a linked list as the underlying data storage mechanism and implement both a stack and a queue.

Features:

- Stack
  - Methods:
    - push
    - pop
    - peek
    - is empty

- Queue
  - Methods
    - enqueue
    - dequeue
    - peek
    - is empty

It raises custom error messages and tests to prove the functionality.

## Whiteboard Process
N/A

## Approach & Efficiency

Resources:
- Various articles and research on stacks and queues
- Adam's demo in Class 10
- ChatGPT

#### Big O

O(1) - constant

Both the Stack and Queue implementations provide constant time operations for their primary methods (push, pop, enqueue, dequeue, peek, and is_empty). This efficiency is one of the key reasons why stacks and queues are widely used in various applications. The constant time complexity (O(1)) for these operations makes them highly efficient for tasks that require frequent additions and removals of elements.
Source: ChatGPT


## Solution
[stack.py](python/data_structures/stack.py)
and [test_stack.py](python/tests/data_structures/test_stack.py)
[queue.py](python/data_structures/queue.py)
and [test_stack.py](python/tests/data_structures/test_queue.py)
