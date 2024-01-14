# Linked List
This project is to implement a linked list using clean, reusable code according to the Single-responsibility principle.

Features
- Node Class: a basic unit with a value and a pointer to the next node.
- Linked List Class: manages the nodes, with methods to insert new nodes at the head with O(1) time complexity, check if a value exists in the list, and convert the list to a string representation.
  - Methods:
    - insert
    - includes
    - to string

It raises custom error messages and tests to prove the functionality.

## Whiteboard Process
N/A

## Approach & Efficiency
Utilized resources available to learn and practice linked list implementation.

Resources:
- Various articles and research on linked lists
- JB's demo in Class 05
- ChatGPT

#### Big O
The most significant factor is the number of nodes in the list.

- Inserting a Node at the Beginning (insert method):
  - Time Complexity: O(1) (Constant Time)
    - involves a few assignment operations, regardless of the list's size.
  - Space Complexity: O(1) (Constant Space)
    - space needed for one new node does not change with the size of the input list.

- Searching for a Value (includes method):
  - Time Complexity: O(n) (Linear Time)
    - might need to traverse the entire list to find the value or conclude it's not there.
    - n represents the number of nodes in the list.
  - Space Complexity: O(1) (Constant Space)
    - space used does not depend on the input size as it only involves a few pointers and variables.

- Creating a String Representation (__str__ method):
  - Time Complexity: O(n) (Linear Time)
    - needs to traverse each node in the list to build the string representation so depends on the number of nodes (n)
  - Space Complexity: O(n) (Linear Space)
    - the space needed to store the string representation is proportional to the number of nodes in the list, as each node's value contributes to the final string.
Source: ChatGPT

## Solution
See [linked_list.py](python/data_structures/linked_list.py)
and [test_linked_list.py](python/tests/data_structures/test_linked_list.py)
