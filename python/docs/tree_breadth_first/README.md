# Tree Breadth First

This project implements a breadth first function taking in tree as an argument and returning a list of all values in the tree in the order they were encountered using a Queue.

Features:
- Queue
  - breadth_first
- Node


## Whiteboard Process
![Whiteboard](/python/docs/tree_breadth_first/codechal-17.png)

## Approach & Efficiency
Reviewed the example, pseudocode and tests provided, whiteboarded test cases and visualized the output. Added the code then used chatgpt to assist on Big O analysis.

#### Resources:

- [Code Fellows' Trees Tutorial and breadth_first pseudocode](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
- JB's intro [Class 17](https://zoom.us/rec/play/vu2fA0oAt_apPPWIqHibndKWKcf0ikQieYclVHkNjNh6LEqaHFZapVWjDytZGGV5DtIARPRux_p0KRWq.YL4FD0AzfO50WERT?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FRFF8xFOEFYHuCXTaet2lxX3ZkT9IHeX_Ha0Psiv_a7NY7nxyQGm_oYjO9nJaDcuT.RaYfajx1j8uC4cRq)


#### Big O

##### BinaryTree
Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited exactly once, making the time complexity linear in the size of the tree.

Space Complexity: O(w), where w is the maximum width of the tree. This represents the worst-case scenario where the queue stores the maximum number of nodes at any level of the tree.

Source: ChatGPT


## Solution
[tree_breadth_first.py](/python/code_challenges/tree_breadth_first.py) and
[queue.py](/python/data_structures/queue.py)

[test_tree_breadth_first.py](/python/tests/code_challenges/test_tree_breadth_first.py) and
[test_queue.py](/python/tests/data_structures/test_queue.py)
