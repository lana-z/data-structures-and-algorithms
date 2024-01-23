# Stacks and Queues
This project is to implement a Queue using two Stacks.

Features:

- Stack
  - Methods:
    - push
    - pop
    - is empty

It raises custom error messages and tests to prove the functionality.

## Whiteboard Process

![Whiteboard](/python/docs/stack_queue_pseudo/codechal-11.png)

## Approach & Efficiency

Resources:
- Code Fellows stacks and queues [article](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html)
- Adam's demo in Class 10
- JB's demo in Class 11
- ChatGPT

#### Big O

The Big O analysis of the `PseudoQueue` class, which uses two stacks to implement queue operations, can be considered for both time and space complexity:

Time Complexity

1. **Enqueue Operation (`enqueue`)**:
   - This operation involves a single `push` to `stack1`, which is an O(1) operation as it simply adds an element to the end of the list.

2. **Dequeue Operation (`dequeue`)**:
   - This operation is more complex. If `stack2` is empty, all elements from `stack1` are moved to `stack2`. This operation is O(n) where n is the number of elements in `stack1`, as each element requires one pop and one push operation.
   - However, each element is moved like this only once. After an element has been moved to `stack2`, it stays there until it is dequeued. So, while a single `dequeue` operation can be O(n) in the worst case (when `stack2` is empty), the average or amortized time complexity for `dequeue` is O(1). This is because each element is moved from `stack1` to `stack2` only once over the course of many `dequeue` operations.

Space Complexity

- The space complexity for the `PseudoQueue` is O(n), where n is the number of elements in the queue. This is because all queue elements must be stored in either `stack1` or `stack2`. The space required grows linearly with the number of elements enqueued.

Summary

- **Enqueue**: O(1) time complexity.
- **Dequeue**: O(1) amortized time complexity, but can be O(n) in the worst case for a single operation.
- **Space Complexity**: O(n) for both enqueue and dequeue operations.

This analysis reflects the trade-off made by using two stacks to implement queue functionality, especially in the dequeue operation, where the amortized time complexity is favorable, but individual operations can occasionally be costlier.

Source: ChatGPT


## Solution
[stack.py](/python/data_structures/stack.py)
and [test_stack.py](/python/tests/data_structures/test_stack.py)

[stack_queue_pseudo.py](/python/code_challenges/stack_queue_pseudo.py)
and [test_stack_queue_pseudo.py](/python/tests/code_challenges/test_stack_queue_pseudo.py)
