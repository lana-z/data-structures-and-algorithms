# Tree Max
(Intro)

Features:

- Binary Search Tree
  - Methods
    - max


## Whiteboard Process



## Approach & Efficiency
Considered how this could work using binary search tree. Whiteboarded the test cases and wrote a plain language algorithm. Attempted the code and used chatgpt as a resource and to assist on Big O analysis.

#### Resources:

- [Code Fellows' Trees Tutorial](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
-
- ChatGPT

#### Big O

##### BinaryTree
Time Complexity: O(n) - Each traversal method (pre-order, in-order, post-order) performs a recursive visit to each node exactly once, where n is the total number of nodes in the tree.

Space Complexity: O(h) in the best case (completely balanced tree) and O(n) in the worst case (completely unbalanced tree, essentially becoming a linked list), where h is the height of the tree. This space complexity accounts for the call stack during recursive calls. In a balanced tree, the height is log(n), leading to a best-case space complexity of O(log(n)).

Source: ChatGPT


## Solution
[binary_search_tree.py](/python/tests/data_structures/test_stack.py)

and [test_binary_search_tree.py](/python/tests/data_structures/test_binary_search_tree.py)
