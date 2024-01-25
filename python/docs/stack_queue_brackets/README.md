# Stack Queue Brackets
This project is to write a function for Multi-bracket Validation with Round Brackets(), Square Brackets[] and
Curly Brackets{}.

Features:
- Queue
  - Methods:
    - enqueue
    - dequeue


## Whiteboard Process

![Whiteboard](/python/docs/stack_queue_brackets/codechal-13.png)

## Approach & Efficiency

Considered how this could work using two queues or a stack and a queue. Whiteboarded the test cases and wrote a plain language algorithm. Attempted the code and used chatgpt to finish the code as well as look at the Big O for both solutions I considered.

#### Resources
- Code Fellows stacks and queues [article](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html)
- ChatGPT
- JB's Class 13 intro to the challenge

#### Big O

Time Complexity
- \(O(n)\) - \(n\) is the length of the input string. Each character in the string is enqueued into the queue and then dequeued once. For each character, a constant time operation is done (either pushing to or popping from the stack) so the number of characters in the string is most relevant.

Space Complexity
- also \(O(n)\) - In the worst-case scenario (when all characters are opening brackets), the stack will store \(n/2\) characters assuming half of the characters in the string are brackets. The queue will temporarily hold all \(n\) characters of the string. So the space used is proportional to the length of the string.

Using two queues instead
- I also looked at ssing Two Queues instead of a stack and a queue. The time complexity of this approach is \(O(n^2)\). This increased complexity arises because, for each closing bracket, the algorithm may have to move all elements from `bracket_queue` to `temp_queue` and back again. In the worst case, this results in a quadratic number of operations relative to the length of the input string. The space complexity remains \(O(n)\) as in the first approach, but with potentially higher constants involved. This is because, in the worst case, all characters in the string might be stored in the queues (either `bracket_queue` or `temp_queue`) at some point during the execution of the algorithm.

Source: ChatGPT


## Solution

[stack_queue_brackets.py](/python/code_challenges/stack_queue_brackets.py)
and [test_stack_queue_brackets.py](/python/tests/code_challenges/test_stack_queue_brackets.py)
