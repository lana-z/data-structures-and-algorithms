# Linked List Kth
This project is to extend linked list implementation with kth from end.

Features

Methods:
  - kth from end


## Whiteboard Process

![Whiteboard](/python/docs/linked_list_kth/codechal-07.png)


## Approach & Efficiency
Defined the problem statement, listed questions to consider, visualized inputs and outputs of test cases, developed a plain language algorithm, wrote the code (see links to code in Solution below), made adjustments.

Resources:
- Various articles and research on linked lists
- My previous [Linked List](/python/docs/codechal-05/README.md) implementations
- ChatGPT

#### Big O

Time:

O(n), where n is the number of nodes in the list. This is because, in the worst case, it traverses the entire list once with the `runner` pointer and then again partially with the `current` pointer.

Space:

O(1), or constant space, because it uses a fixed amount of extra space two pointers, `current` and `runner`, regardless of the size of the input list. The function is efficient in terms of space and has a linear time complexity relative to the size of the linked list.


## Solution
See [linked_list.py](/python/data_structures/linked_list.py)
and [test_linked_list_kth.py](/python/tests/code_challenges/test_linked_list_kth.py)

