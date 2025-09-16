class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        """
        Initialize an empty linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self):
        """
        Method to print LinkedList values
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.
        :param value: The value to be added to the linked list.
        """
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def pop(self):
        """
        Remove and return the last node's value from the linked list.
        :return: The last node, or None if the list is empty.
        """
        if self.head is None:
            return None
        
        node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            index = 1
            pre_node = self.head
            while index < self.length - 1:
                pre_node = pre_node.next
                index += 1
            
            self.tail = pre_node
            self.tail.next = None

        self.length -= 1
        return node
    
    def prepend(self, value):
        """
        Add a new node with the given value to the beginning of the linked list.
        :param value: The value to be added to the linked list.
        """
        if self.head is None:
            self.append(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.length += 1

    def pop_first(self):
        """
        Remove and return the first node's value from the linked list.
        :return: The first node, or None if the list is empty.
        """
        if self.head is None or self.length == 1:
            return self.pop()

        node = self.head
        self.head = self.head.next
        node.next = None
        self.length -= 1
        return node
    
    def get(self, index):
        """
        Get the value of the node at the specified index.
        :param index: The index of the node to retrieve.
        :return: The node at the specified index, or None if the index is out of bounds.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index < 0 or index >= self.length:
            return None
        
        current, i = self.head, 0
        while i != index:
            current = current.next
            i += 1
        return current
    
    def set_value(self, index, value):
        """
        Set the value of the node at the specified index.
        :param index: The index of the node to update.
        :param value: The new value to set for the node.
        """
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        """
        Insert a new node with the given value at the specified index.
        :param index: The index at which to insert the new node.
        :param value: The value to be added to the linked list.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            node = Node(value)
            pre_node = self.get(index - 1)
            node.next = pre_node.next
            pre_node.next = node
            self.length += 1
        
        return True
    
    def remove(self, index):
        """
        Remove the node at the specified index.
        :param index: The index of the node to remove.
        :return: The removed node, or None if the index is out of bounds.
        """
        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        pre_node = self.get(index - 1)
        node = pre_node.next
        pre_node.next = node.next
        node.next = None
        self.length -= 1
        return node
    
    def reverse(self):
        """
        Reverse the linked list in place.
        """
        if self.head is None or self.length == 1:
            return
        
        current = self.head
        self.head = self.tail
        self.tail = current
        pre = None
        post = current.next

        for _ in range(self.length):
            post = current.next
            current.next = pre
            pre = current
            current = post

    def find_middle_node(self):
        """
        Find the middle node of the linked list.
        :return: The middle node, or None if the list is empty.
        """
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        """
        Check if the linked list has a loop.
        Floyd's cycle-finding algorithm / Tortoise and Hare algorithm.
        :return: True if there is a loop, False otherwise.
        """
        if self.head is None:
            return False
        
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
    
    def kth_node_from_end(self, k):
        """
        Find the k-th node from the end of the linked list assuming no length parameter.
        This method uses the two-pointer technique to find the k-th node from the end.
        :raises TypeError: If k is not a positive integer.
        :param k: The position from the end of the list (1-based).
        :return: The k-th node from the end, or None if k is out of bounds.
        """
        if not isinstance(k, int) or k <= 0:
            raise TypeError("k must be a positive integer")

        slow = self.head
        fast = self.head
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next
        return slow
    
    def remove_duplicates(self):
        """
        Remove duplicate values from the linked list.
        This method uses a set to track seen values.
        """
        values = set()
        previous = None
        current = self.head
        while current:
            if current.value in values:
                previous.next = current.next
                self.length -= 1
            else:
                values.add(current.value)
                previous = current
            current = current.next

    def binary_to_decimal(self):
        """
        Convert a binary linked list to its decimal equivalent.
        :return: The decimal value of the binary linked list.
        """
        num = 0
        current = self.head
        while current:
            num = num * 2 + current.value
            current = current.next
        return num
    
    def partition_list(self, x):
        """        
        Partition the linked list into two parts: nodes with values less than x and nodes with values greater than or equal to x.
        :param x: The value to partition the list around.
        This method rearranges the nodes in place without creating new nodes.
        :return: None
        1. Create two dummy nodes to hold the two partitions.
        2. Traverse the original list and append nodes to the appropriate partition based on their value.
        3. Connect the end of the first partition to the start of the second partition.
        4. Update the head of the linked list to the start of the first partition.
        5. Ensure the last node of the second partition points to None.
        6. Handle edge cases where the list is empty or has only one node.
        7. Time complexity: O(n), where n is the number of nodes in the linked list.
        8. Space complexity: O(1), as we are not using any additional data structures that grow with input size.
        9. This method modifies the original linked list in place.
        10. The order of nodes in each partition is preserved.
        11. This method does not return a new linked list but modifies the existing one.
        """
        if not self.head or not self.head.next:
            return
        
        dummy_1 = Node(0)
        dummy_2 = Node(0)
        
        pre_1 = dummy_1
        pre_2 = dummy_2
        
        node = self.head
        while node is not None:
            if node.value < x:
                pre_1.next = node
                pre_1 = node
            else:
                pre_2.next = node
                pre_2 = node
             
            node = node.next
        
        pre_2.next = None
        pre_1.next = dummy_2.next
        self.head = dummy_1.next

    def reverse_between(self, start_index, end_index):
        """        
        Reverse the nodes of the linked list from start_index to end_index (inclusive).
        :param start_index: The starting index of the sublist to reverse (0-based).
        :param end_index: The ending index of the sublist to reverse (0-based).
        :return: None
        This method reverses the nodes in place without creating new nodes.
        1. Handle edge cases where the list is empty or has only one node.
        2. If start_index is greater than or equal to end_index, do nothing.
        3. Traverse the list to find the nodes at start_index and end_index.
        4. Reverse the nodes between start_index and end_index by adjusting their next pointers.
        5. Connect the reversed sublist back to the main list.
        6. Update the head of the linked list if necessary.
        7. Time complexity: O(n), where n is the number of nodes in the linked list.
        8. Space complexity: O(1), as we are not using any additional data structures that grow with input size.
        9. This method modifies the original linked list in place.
        10. The order of nodes outside the reversed sublist remains unchanged.
        11. This method does not return a new linked list but modifies the existing one.

        Best solution

        if not self.head or start_index >= end_index:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        # Move prev to the node before start_index
        for _ in range(start_index):
            prev = prev.next
        
        # Start reversing from start_index
        current = prev.next
        
        # Reverse the sublist
        for _ in range(end_index - start_index):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        # Update head if necessary
        self.head = dummy.next
        """

        if not self.head or not self.head.next or start_index >= end_index:
            return
        
        index = 0
        pre = None
        pre_start = start = end = post_end = None
        current = self.head
        
        while current:
            post = current.next
            if index == start_index:
                pre_start = pre
                start = current
            elif index == end_index:
                end = current
                post_end = post
            
            if start_index + 1 <= index <= end_index:
                current.next = pre
            
            index += 1   
            pre = current
            current = post
            
        if pre_start:
            pre_start.next = end
        else:
            self.head = end
            
        start.next = post_end

    def swap_pairs(self):
        """        
        Swap every two adjacent nodes in the linked list.
        :return: None
        This method swaps nodes in pairs without creating new nodes.
        1. Handle edge cases where the list is empty or has only one node.
        2. Create a dummy node to simplify the swapping logic.
        3. Use a pointer to track the previous node to facilitate swapping.
        4. Traverse the list in pairs and swap the nodes by adjusting their next pointers.
        5. Update the head of the linked list to the new first node after swapping.
        6. Ensure the last node of the swapped pair points to None.
        7. Time complexity: O(n), where n is the number of nodes in the linked list.
        8. Space complexity: O(1), as we are not using any additional data structures that grow with input size.
        9. This method modifies the original linked list in place.
        10. The order of nodes within each pair is reversed.
        11. This method does not return a new linked list but modifies the existing one.
        """
        
        if not self.head or not self.head.next:
            return
        
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            prev.next = second
            first.next = second.next
            second.next = first
            
            prev = first
        
        self.head = dummy.next
        dummy.next = None


if __name__ == "__main__":
    ...

