"""
This module provides a set of functions for working with hash tables.
Terminology:
- Hash Table: A data structure that maps keys to values for efficient lookup.
- Hash Function: A function that converts a key into an index in the hash table.
- Collision: When two keys hash to the same index.
- Load Factor: The ratio of the number of elements to the size of the hash table.
- Chaining: A collision resolution strategy that uses linked lists to store multiple values at the same index.
- Open Addressing: A collision resolution strategy that finds another open slot in the hash table.
"""

class HashTable:
    """
    A simple hash table implementation using chaining for collision resolution.
    """
    def __init__(self, size=7):
        self.size = size
        self.data_map = [None] * size

    def __hash(self, key):
        """        
        A simple hash function that computes the hash of a key.
        Args:
            key: The key to hash.
        Returns:
            int: The index in the hash table where the key-value pair should be stored.
        
        manuel hash function
        hash_value = 0
        for char in key:
            hash_value = hash_value + ord(char)*31
        return hash_value % self.size
        """
        return hash(key) % self.size

    def set_item(self, key, value):
        """
        Inserts or updates a key-value pair in the hash table.
        If the key already exists, it updates the value.
        If the key does not exist, it creates a new entry.
        Args:
            key: The key to insert or update.
            value: The value associated with the key.
        """
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []

        for i, kv in enumerate(self.data_map[index]):
            if kv[0] == key:
                kv[1] = value
                return
            
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """
        Retrieves the value associated with a key in the hash table.
        If the key does not exist, it returns None.
        Args:
            key: The key to retrieve.
        Returns:
            The value associated with the key, or None if the key does not exist.
        """
        index = self.__hash(key)

        if self.data_map[index] is not None:
            for kv in self.data_map[index]:
                if kv[0] == key:
                    return kv[1]
        return None
    
    def keys(self):
        """
        Returns a list of all keys in the hash table.
        Returns:
            list: A list of keys in the hash table.
        """
        keys = []
        for bucket in self.data_map:
            if bucket is not None:
                for kv in bucket:
                    keys.append(kv[0])
        return keys
