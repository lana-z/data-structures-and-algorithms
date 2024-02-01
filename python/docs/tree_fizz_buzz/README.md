# Tree Fizz Buzz

This project implements a function to play FizzBuzz taking in a K-ary Tree and returning a new K-ary Tree and runs tests on the funcitons.

Features:
- fizz_buzz
- fizz_buzz_tree
- [KaryTree](/python/data_structures/kary_tree.py)
  - breadth_first
  - clone
  - Node

## Whiteboard Process
![Whiteboard](/python/docs/tree_fizz_buzz/codechal-18.png)

## Approach & Efficiency
Reviewed the problem and tests provided, whiteboarded test cases and visualized the output. Added the code then used chatgpt to assist on Big O analysis.

#### Resources:

- [Code Fellows' Trees Tutorial and breadth_first pseudocode](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
- JB's intro and Kary tree class(/python/data_structures/kary_tree.py)


#### Big O
Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once, making the time complexity linear to the size of the tree.

Space Complexity: O(n), where n is the number of nodes in the tree. The space is the same as the argument tree’s space.


## Solution
[tree_fizz_buzz.py](/python/code_challenges/tree_fizz_buzz.py)

[test_tree_fizz_buzz.py](/python/tests/code_challenges/test_tree_fizz_buzz.py)
