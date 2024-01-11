
# Array Binary Search
401 Class 03

## Whiteboard Process
![Whiteboard](/python/docs/codechal-03/codechal-03.png)

## Approach & Efficiency
Defined the problem statement, listed questions to consider, visualized inputs and outputs of test cases, developed a plain language algorithm, attempted code, enlisted help of chatGPT, edited plain language algo, wrote the code, not sure if code is correct because it's not returning anything in Replit.

#### Big O

Time
- binary search depends on the length of the array

Space
- not creating a new array or modifying, simply looking for value matching the search key and returning a constant, the index if found, -1 if not found.

Source: [bigocalc.com](https://www.bigocalc.com/)
The time complexity of the BinarySearch function is O(log n), where n is the length of the input array. This is because the function uses a binary search algorithm, which repeatedly divides the search space in half until the key is found or the search space is empty. Each iteration of the binary search reduces the search space by half, resulting in a logarithmic time complexity.

The space complexity of the BinarySearch function is O(1) because it uses a constant amount of additional space. The function only uses a few variables to keep track of the left and right indices, the mid index, and the key, and does not create any additional data structures or use recursion. Therefore, the space complexity is constant.


## Solution

```python
def binary_search(arr, key):
  left = 0
  right = len(arr) - 1

  while left <= right:
      mid = left + (right - left) // 2
        if arr[mid] == key:
          return mid
        if arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```
TBC
