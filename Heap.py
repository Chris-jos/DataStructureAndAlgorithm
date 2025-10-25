"""
A simple implementation of a min-heap data structure.
What is a Heap?
- A specialized tree-based data structure that satisfies the heap property.
- In a min-heap, for any given node, the value of the node is less than or equal to the values of its children.
- In a max-heap, for any given node, the value of the node is greater than or equal to the values of its children.
- Commonly used to implement priority queues, where the highest (or lowest) priority element is always at the front.
- Identifying heap list indexes: (1-based index)
    - Left Child: 2 * parent Index
    - Right Child: 2 * parent Index + 1
    - Parent: floor(child Index / 2)
"""

import heapq


class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sink_down(self, index):
        """
        Sinks down the value at the given index to its proper position in the heap.
        """
        while True:
            left = self._left_child(index)
            right = self._right_child(index)
            largest = index

            if left < len(self.heap) and self.heap[left] > self.heap[largest]:
                largest = left
            if right < len(self.heap) and self.heap[right] > self.heap[largest]:
                largest = right
            if largest == index:
                break
            self._swap(index, largest)
            index = largest

    def insert(self, value):
        """
        Inserts a new value into the heap.
        Args:
            value: The value to insert.
        """
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        """
        Removes and returns the maximum value from the heap.
        Returns:
            The maximum value in the heap.
        """
        if len(self.heap) == 0:
            raise IndexError("remove from empty heap")
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return root


# Heap using in built library
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """
        Inserts a new value into the heap.
        Args:
            value: The value to insert.
        """
        heapq.heappush(self.heap, value)

    def remove(self):
        """
        Removes and returns the minimum value from the heap.
        Returns:
            The minimum value in the heap.
        """
        if len(self.heap) == 0:
            raise IndexError("remove from empty heap")
        return heapq.heappop(self.heap)


if __name__ == "__main__":
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(5)
    max_heap.insert(30)
    print(max_heap.heap)  # Output: [30, 20, 5, 10]
    print(max_heap.remove())  # Output: 30
    print(max_heap.heap)  # Output: [20, 10, 5]
