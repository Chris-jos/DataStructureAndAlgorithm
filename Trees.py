"""
This module provides a set of functions for working with binary trees.
Terminology:
- Node: A single element in the tree containing a value and references to left and right children
- Tree: A collection of nodes where each node can have up to two children
- Leaf: A node that does not have any children
- Height: The length of the longest path from the root to a leaf node
- Depth: The length of the path from the root to a specific node
- full binary tree: A tree where every node other than the leaves has two children
- perfect binary tree: A full binary tree where all leaves are at the same level
- complete binary tree: A binary tree where all levels are fully filled except possibly for the last level, which is filled from left to right
- binary search tree: A binary tree where for each node, all values in the left subtree are less than the node's value, and all values in the right subtree are greater than the node's value
"""

class Node:
    """
    A class representing a node in a binary tree.
    Each node contains a value and references to its left and right children.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    A class representing a binary search tree.
    It provides methods to insert values, search for values,
    and traverse the tree in various orders (in-order, pre-order, post-order).
    """
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the binary search tree.
        """
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        
        temp = self.root
        while True:
            if value == temp.value:
                return False
            
            if value < temp.value:
                if temp.left is None:
                    temp.left = node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = node
                    return True
                temp = temp.right
        
    def contains(self, value):
        """
        Checks if the binary search tree contains a specific value.
        """
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
