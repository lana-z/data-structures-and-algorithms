# Hash Table Data Structure
This project is to implement a hash table.

## Whiteboard
![Whiteboard](/python/docs/hashtable/codechal-30.png)


## Approach & Efficiency

Resources:
- [Hashtables](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-30/resources/Hashtables.html)
- My previous [Linked List](https://github.com/lana-z/data-structures-and-algorithms/blob/main/python/data_structures/linked_list.py) implementation
- JB's Hashtables demo
- ChatGPT

#### Big O

##### Space Complexity:

- **Overall Space Complexity**: \( O(N + M) \) where \( N \) is the number of key-value pairs stored in the hash table and \( M \) is the size of the underlying array (in this case, `self._buckets`). The space for the hash table is dominated by the space needed to store all the entries (key-value pairs) and the overhead of the array used for the buckets.

- The space complexity is primarily determined by the number of entries and the size of the array used for the buckets.

##### Time Complexity:

1. **`__init__` method**: \( O(M) \)
   - Initializing the hash table involves creating an array of size `M` (`self._buckets`). Each element of the array is initially set to `None`, leading to a linear time complexity proportional to the size of the array.

2. **`set` method**: Average \( O(1) \), Worst-case \( O(N) \)
   - In the average case, assuming a good hash function and relatively even distribution of keys across the buckets, inserting a new key-value pair is constant time since it involves computing the hash, accessing the corresponding bucket, and inserting the new node at the beginning of the linked list.
   - In the worst-case scenario, where all keys hash to the same bucket, the time complexity becomes linear \( O(N) \) because the method would have to traverse the entire linked list to insert or update a key-value pair.

3. **`get` method**: Average \( O(1) \), Worst-case \( O(N) \)
   - Similar to the `set` method, retrieving a value by key is constant time in the average case due to the efficient hash and distribution of keys.
   - In the worst-case scenario where all keys are in the same bucket, the time complexity is \( O(N) \) as it may need to traverse the entire linked list to find the key.

4. **`keys` method**: \( O(N) \)
   - This method requires traversing all buckets and all the entries within each bucket's linked list to collect all keys. Therefore, its time complexity is linear with respect to the number of key-value pairs in the hash table.

5. **`has` method**: Average \( O(1) \), Worst-case \( O(N) \)
   - Checking the existence of a key is similar to the `get` method in terms of complexity, with average constant time and worst-case linear time if all keys are in the same bucket.

6. **`_hash` method**: \( O(K) \)
   - The hash function's time complexity is proportional to the length of the key \( K \), as it iterates over each character to compute the hash value.

- The average case time complexity for most operations (`set`, `get`, and `has`) is \( O(1) \), which is ideal for a hash table.
- The worst-case time complexity can degrade to \( O(N) \) for these operations if the keys are not evenly distributed across the buckets, leading to long linked lists.

Source: ChatGPT

## Solution

See [hashtable.py](python/data_structures/hashtable.py)
and [test_hashtable.py](python/tests/code_challenges/test_hashtable.py)
