# Array Binary Search
401 Class o4

## Whiteboard Process
![Whiteboard](/python/docs/codechal-04/codechal-04.png)

## Approach & Efficiency
Defined the problem statement, listed questions to consider, visualized inputs and outputs of test cases, developed a plain language algorithm, wrote the code in Replit, consulted chatgpt and adjusted until successful.

#### Big O

Source: chatgpt

Time
- If the matrix has n rows, the outer loop runs n times.
- For each row, the inner loop iterates over each element. If each row has an average of m elements, the inner loop runs m times for each row.
- The time complexity of the sum_of_rows function is O(n * m), where n is the number of rows and m is the average number of elements in each row.
- This complexity is considered linear with respect to the total number of elements in the matrix. However, it's important to note that this is not simply O(n) or O(m) because the total number of operations depends on both the number of rows and the number of elements in each row.

Space
- The additional space required by the sum_of_rows function is primarily dependent on the number of rows in the matrix. Therefore, the space complexity is O(n), where n is the number of rows in the matrix.


## Solution

Link to my [Replit](https://replit.com/@lana41/MatrixArraySums#main.py)

```
def sum_of_rows(matrix):
  sums = []
  for row in matrix:
    row_sum = 0
    for element in row:
        if element is None:
            element = 0
        row_sum += element
    sums.append(row_sum)
  return sums

print(sum_of_rows([[1,2,3,4], [6,3,None,2], [-5, 9, -8, 7, 0]]))

```
