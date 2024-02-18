from data_structures.linked_list import LinkedList


class Hashtable:
    """
    This hash table is for storing and retrieving key-value pairs. It uses an array of linked lists or none (buckets) to store the pairs (drops).

    The number of buckets in the hash table is set to 1024.
    """

    def __init__(self, size=1024):
        """
        initializes the hash table
        """
        self._size = size
        self._buckets = [None] * size

    def set(self, key, value):
        """
        inserts or updates a key-value pair in the hash table
        """

        index = self._hash(key)
        bucket = self._buckets[index]
        if bucket is None:
            bucket = LinkedList()
            self._buckets[index] = bucket

        current = bucket.head

        while current:
            candidate_drop = current.value

            # checking to see if the specific key is already there in one of the buckets
            if candidate_drop[0] == key:
                # if so, update the value instead of adding a new drop at the head node.
                candidate_drop[1] = value
                return

        # if the specific key isn't found, add the drop aka key-value pair
        drop = [key, value]
        bucket.insert(drop)

    def get(self, key):
        """
        gets the value of a key from the hash table, or None if the key isn't there
        """

        index = self._hash(key)

        bucket = self._buckets[index]

        if bucket is None:
            return None

        current = bucket.head

        while current:
            drop = current.value
            if drop[0] == key:
                return drop[1]

            current = current.next

        return None

    def keys(self):
        """
        rturns a list of all the keys stored in the hash table
        """
        key_list = []

        for bucket in self._buckets:  # list of LinkedLists (or None)
            if bucket:  # LinkedList
                current = bucket.head  # Node
                while current:
                    drop = current.value  # List of 2 items [key, value]
                    key_list.append(drop[0])
                    current = current.next

        return key_list

    def has(self, key):
        """
        checks if a given key is in the hash table and returns boolean true or false
        """
        for bucket in self._buckets:
            if bucket:
                current = bucket.head
                while current:
                    drop = current.value
                    if drop[0] == key:
                        return True

                    current = current.next

        return False

    def _hash(self, key):
        """
        private method that computes the hash value of a given key by:
        Add all the ASCII values together.
        Multiply it by a prime number such as 599.
        Use modulo to get the remainder of the result, when divided by the total size of the array.
        """
        index = 0
        for char in key:
            index += ord(char)
        index *= 599
        index = index % self._size

        return index
