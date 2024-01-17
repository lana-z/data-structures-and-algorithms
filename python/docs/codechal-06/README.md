# Linked List Insertions
This project is to extend linked list implementation with insertions using the Single responsiblity principle.

Features

Methods:
  - append
  - insert before
  - insert after

It raises custom error messages and tests to prove the functionality.

## Whiteboard Process

![Whiteboard](/python/docs/codechal-06/codechal-06.png)


## Approach & Efficiency
Defined the problem statement, listed questions to consider, visualized inputs and outputs of test cases, developed a plain language algorithm, wrote the code (see links to code in Solution below), made adjustments.

Resources:
- Various articles and research on linked lists
- My previous [Linked List](python/docs/codechal-05/README.md) code challenge
- JB's Class 06 explainer
- ChatGPT

#### Big O
The most significant factor is the number of nodes in the list.

- Inserting a Node at the End (append method):
  - Time Complexity: O(1) (Constant Time)
    - involves a few assignment operations, regardless of the list's size.
  - Space Complexity: O(1) (Constant Space)
    - space needed for one new node does not change with the size of the input list.

- Searching for a Value (insert methods):
  - Time Complexity: O(n) (Linear Time)
    - might need to traverse the entire list to find the value or conclude it's not there.
    - n represents the number of nodes in the list.
  - Space Complexity: O(1) (Constant Space)
    - space used does not depend on the input size as it only involves a few pointers and variables.


## Solution
See [linked_list.py](python/data_structures/linked_list.py)
and [test_linked_list_insertions.py](python/tests/code_challenges/test_linked_list_insertions.py)
