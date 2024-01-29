# Stacks and Queues
This project is to implement a Binary Tree and a Binary Search Tree.

Features:

- Binary Tree
  - Methods:
    - pre_order
    - in_order
    - post_order
    - walk

- Binary Search Tree
  - Methods
    - add
    - contains


## Whiteboard Process
N/A


## Approach & Efficiency

#### Resources:

- [Code Fellows' Trees Tutorial](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
- JB's demo in Class 15
- ChatGPT

#### Big O

##### BinaryTree
Time Complexity: O(n) - Each traversal method (pre-order, in-order, post-order) performs a recursive visit to each node exactly once, where n is the total number of nodes in the tree.

Space Complexity: O(h) in the best case (completely balanced tree) and O(n) in the worst case (completely unbalanced tree, essentially becoming a linked list), where h is the height of the tree. This space complexity accounts for the call stack during recursive calls. In a balanced tree, the height is log(n), leading to a best-case space complexity of O(log(n)).

##### BinarySearchTree

*Add*
Time Complexity: Average Case for add: O(log n), where n is the number of nodes in the tree. This assumes that the tree is balanced, allowing you to eliminate half of the remaining subtree at each step. Worst Case: O(n), in the case of an unbalanced tree where the elements are added in such a manner that the tree becomes a straight line (like a linked list).

Space Complexity: O(h) for recursive stack space, where h is the height of the tree. This is log(n) in the average case for a balanced tree and O(n) in the worst case for a skewed tree.

*Contains*
Time Complexity:
Average Case for contains/search: O(log n), under the assumption that the tree is balanced. Each comparison allows the algorithm to skip half of the remaining tree, so the time complexity is logarithmic. Worst Case: O(n), in an unbalanced tree, where the search might have to traverse from the root to the deepest leaf node.

Space Complexity: Similar to the add operation, the space complexity is O(h) due to recursive calls, where h is the height of the tree. This evaluates to O(log n) in a balanced tree and O(n) in the worst-case scenario of an unbalanced tree.

Source: ChatGPT


## Solution
[binary_tree.py](/python/data_structures/stack.py)
and [binary_search_tree.py](/python/tests/data_structures/test_stack.py)

[test_binary_tree.py](/python/tests/data_structures/test_binary_tree.py)
and [test_binary_search_tree.py](/python/tests/data_structures/test_binary_search_tree.py)

custom error [invalid opperation error](/python/data_structures/invalid_operation_error.py)
