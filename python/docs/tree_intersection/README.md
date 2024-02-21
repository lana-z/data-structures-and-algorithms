# Tree Intersection
This project is to find common values in 2 binary trees.

Features:
- Queue
  - Methods:
    - enqueue
    - dequeue
- Classes and Super Class (Animal)

## Whiteboard Process

![Whiteboard](/python/docs/tree_intersection/codechal-32.png)

## Approach & Efficiency

#### Resources
- Code Fellows hashtables [article](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-30/resources/Hashtables.html)
- My previous [hashtable](/python/data_structures/hashtable.py) implementation
- ChatGPT


#### Big O

Time Complexity
 - The traversal of both trees, which is O(N + M) where N and M are the number of nodes in tree_a and tree_b, respectively. The time operations for hashtable lookups and set insertions are  constant.

Space Complexity
- Considering the space for the hashtable and the result set, the maximum space complexity would be O(N + K) where K is the number of common elements stored in the result set.

Source: ChatGPT


## Solution

[tree_intersection.py](/python/code_challenges/tree_intersection.py)
and [test_tree_intersection.py](/python/tests/code_challenges/test_tree_intersection.py)
