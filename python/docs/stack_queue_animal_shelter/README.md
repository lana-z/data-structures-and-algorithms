# Stack Queue Animal Shelter
This project is to create an Animal Shelter app using Stack and Queue data structures.

Features:

- Stack
  - Methods:
    - push
    - pop
    - is empty
- Queue
  - Methods:
    - enqueue
    - dequeue

It raises custom error messages and tests to prove the functionality.

## Whiteboard Process

![Whiteboard](/python/docs/stack_queue_animal_shelter/codechal-12.png)

## Approach & Efficiency

Resources:
- Code Fellows stacks and queues [article](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-10/resources/stacks_and_queues.html)
- JB's cereal [demo](https://github.com/codefellows/seattle-code-python-401d24/blob/main/class-12/demo/cereals-demo.ipynb) in Class 12
- ChatGPT

#### Big O

Time Complexity
 - constant, O(1). This means the performance of these operations will remain consistent regardless of the number of animals in the shelter.
Space Complexity
- linear, O(n), where n is the total number of animals (dogs and cats) in the shelter. This is because the space used by the shelter is directly proportional to the number of animals it holds at any given time.

Source: ChatGPT


## Solution
Code isn't passing tests yet.
[stack_queue_animal_shelter.py](/python/code_challenges/stack_queue_animal_shelter.py)
and [test_stack_queue_animal_shelter.py](/python/tests/code_challenges/test_stack_queue_animal_shelter.py)
