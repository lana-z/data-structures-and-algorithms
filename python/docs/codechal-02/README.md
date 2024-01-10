
# Insert Shift Array
401 Class 02

## Whiteboard Process
![Whiteboard](/python/docs/codechal-02/codechal-02.png)

## Approach & Efficiency
Defined the problem statement, listed questions to consider, visualized inputs and outputs of test cases, developed a plain language algorithm, attempted code, enlisted help of chatGPT and Tammy, edited plain language algo, wrote the code.

#### Big O
Time
- Finding halves
  - single step operations so does not depend on how big the array is: N
- Linear time complexity

Space
- Creating a new array


"The code snippet has a linear time complexity of O(n) because it iterates through the list to find the middle index, which takes O(n/2) time. Then, it creates a new list by concatenating the left half, the value, and the right half, which also takes O(n/2) time. Therefore, the overall time complexity is O(n/2) + O(n/2), which simplifies to O(n)."
Source: [timecomplexity.ai](https://www.timecomplexity.ai/?id=82448377-2621-48f6-9977-aa87c6eab74f)


## Solution

Link to my [Replit](https://replit.com/@lana41/Codechal-02#main.py)

```python

def reverse_list(items):
  left_index = 0
  right_index = len(items) - 1
  while left_index < right_index:
    items[left_index], items[right_index] = items[right_index], items[left_index]
    left_index += 1
    right_index -= 1

  return items

```
