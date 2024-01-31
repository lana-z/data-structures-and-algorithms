# Tree Max
(Intro)

Features:

- Binary Tree
  - Methods
    - find_maximum_value


## Whiteboard Process
![]()


## Approach & Efficiency
Considered how this could work using binary search tree. Whiteboarded the test cases and wrote a plain language algorithm. Attempted the code and used chatgpt as a resource and to assist on Big O analysis.

#### Resources:

- [Code Fellows' Trees Tutorial](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-15/resources/Trees.html)
- JB's code review [Class 17](https://zoom.us/rec/play/vu2fA0oAt_apPPWIqHibndKWKcf0ikQieYclVHkNjNh6LEqaHFZapVWjDytZGGV5DtIARPRux_p0KRWq.YL4FD0AzfO50WERT?canPlayFromShare=true&from=share_recording_detail&continueMode=true&componentName=rec-play&originRequestUrl=https%3A%2F%2Fzoom.us%2Frec%2Fshare%2FRFF8xFOEFYHuCXTaet2lxX3ZkT9IHeX_Ha0Psiv_a7NY7nxyQGm_oYjO9nJaDcuT.RaYfajx1j8uC4cRq)
- ChatGPT

#### Big O

##### BinaryTree
Time Complexity: O(n) - \(O(n)\), where \(n\) is the number of nodes in the tree. This is because the function performs a depth-first search, visiting each node exactly once to compare its value against the current maximum found.

Space Complexity: \(O(h)\), where \(h\) is the height of the tree. This space is used by the call stack due to recursion. In the worst-case scenario (a degenerate or unbalanced tree), the height of the tree can become \(n\), leading to a worst-case space complexity of \(O(n)\). For a balanced tree, the height \(h\) would be \(\log n\), leading to a more efficient space complexity of \(O(\log n)\).

Source: ChatGPT


## Solution
[binary_tree.py](/python/data_structures/binary_tree.py)

and [test_binary_tree.py](/python/tests/data_structures/test_binary_tree.py)
