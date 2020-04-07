# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        return f"<{self.key}, {self.value}>"


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.entries = 0
        self.storage = [None] * capacity

    def _hash(self, key):
        """
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        """
        return hash(key)

    def _hash_djb2(self, key):
        """
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        """
        pass

    def _hash_mod(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        """
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        """

        # # Resize if # of entries reaches capacity
        # if self.entries >= self.capacity:
        #     self.resize()

        # Hash to find bucket/index
        key_index = self._hash_mod(key)

        pair = self.storage[key_index]

        if pair is not None:
            currPair = pair
            while currPair is not None:
                if currPair.key == key:
                    # Found our pair
                    currPair.value = value
                    break

                if currPair.next == None:
                    # We reached the end, make new pair.
                    newPair = LinkedPair(key, value)
                    currPair.next = newPair
                    self.entries += 1
                    break
                else:
                    currPair = currPair.next
        else:
            self.storage[key_index] = LinkedPair(key, value)
            self.entries += 1

    def remove(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        """
        key_index = self._hash_mod(key)
        if self.storage[key_index] is not None and self.storage[key_index].key == key:
            self.storage[key_index] = None
        else:
            previousPair = self.storage[key_index]
            currPair = previousPair.next
            while currPair is not None:
                if currPair.key == key:
                    # Found
                    # 'Remove'
                    previousPair.next = currPair.next
                    break

                # Reached the end
                if currPair.next is None:
                    print("Warning: key not found when trying to remove.")
                    break
                else:
                    previousPair = currPair
                    currPair = currPair.next

    def retrieve(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        """
        key_index = self._hash_mod(key)
        if self.storage[key_index] is not None:

            currPair = self.storage[key_index]
            while currPair is not None:
                if currPair.key == key:
                    # found
                    return currPair.value
                else:
                    currPair = currPair.next

            # Not found in loop
            return None
        else:
            return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        """
        self.capacity *= 2
        newArr = [None] * self.capacity
        oldArr = self.storage
        self.storage = newArr

        # Traverse through old array
        for elem in oldArr:
            if elem is not None:
                nextPair = elem
                # Loop to the end of the linked pairs if there are any
                while nextPair is not None:
                    # Copy contents to new Array with new hash indexes/buckets
                    self.insert(nextPair.key, nextPair.value)
                    nextPair = nextPair.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
