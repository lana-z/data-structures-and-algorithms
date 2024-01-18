# Linked List Zip
This project is to zip two linked lists.

## Whiteboard
![Whiteboard](/python/docs/linked_list_zip/codechal-08.png)


## Approach & Efficiency
Defined the problem statement, listed questions to consider, visualized inputs, outputs and test cases, developed a plain language algorithm, attempted the code (see links to code in Solution below). 


Resources:
- Various articles and research on linked lists
- My previous [Linked List](https://github.com/lana-z/data-structures-and-algorithms/blob/main/python/data_structures/linked_list.py) implementations
- ChatGPT

#### Big O
The most significant factor is the number of nodes in the two argument lists. The function iterates through both linked lists.
  - Time Complexity: O(1) (Constant Time)
    - list a has x items and list b has y items, then the time complexity is linear O(x+y)
  - Space Complexity: O(1) (Constant Space)
    - new linked list is created as the two lists are zipped and is linear adding the number of elements

## Solution
See [linked_list.py](python/data_structures/linked_list.py)
and [test_linked_list_zip.py](python/tests/code_challenges/test_linked_list_zip.py)
 - 2 of 5 tests passing
