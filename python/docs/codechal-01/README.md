
# Array Reverse
401 Class 01

## Whiteboard Process
![Array Reverse Whiteboard v1](/python/docs/codechal-01/codechal-01.png)

![Array Reverse Whiteboard v2](/python/docs/codechal-01/codechal-01.v2.png)

- v.2 Reference: class 02 code review with JB

## Approach & Efficiency
Time
- Go through the number of half the list items to get to midpoint
time depends on how big the list is
single step operations so operations do not depend on how big the array is (O of 1 operations)
swapping
incrementing/modifying the right and left indices
- .5 n since go through half the list
- Big O notation, drop the .5
- n since time is related to n (the length of n/the items)
- Linear time complexity

Space
- Not creating a new array
- a little bit of memory allocated but constant since only 1 left and 1 right index no matter how long the array is
- O of 0
- The algorithm uses a fixed amount of space regardless of the input size

Time Complexity: O(N)
Space Complexity: O(1)

## Solution
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
