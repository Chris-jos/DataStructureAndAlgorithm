class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """ 
    A class representing a doubly linked list with basic operations. 
    """
    def __init__(self):
        """
        Initializes an empty doubly linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0
    
    def print_list(self):
        """
        Method to print DoublyLinkedList values
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.
        :param value: The value to be added to the list.
        """
        node = Node(value)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev =  self.tail
            self.tail = node

        self.length += 1

    def pop(self):
        """
        Removes and returns the last node of the list.
        :return: The last node of the list or None if the list is empty.
        :rtype: Node or None
        """
        if not self.head:
            return None

        node = self.tail
        if self.length == 1:
            self.tail = self.head = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            node.prev = None

        self.length -= 1
        return node
    
    def prepend(self, value):
        """
        Prepends a new node with the given value to the start of the list.
        :param value: The value to be added to the start of the list.
        """
        if self.head is None:
            self.append(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head.prev = node
            self.head = node
            self.length += 1
    
    def pop_first(self):
        """
        Removes and returns the first node of the list.
        :return: The first node of the list or None if the list is empty.
        :rtype: Node or None
        """
        if self.length <= 1:
            return self.pop()

        node = self.head
        self.head = self.head.next
        self.head.prev = None
        node.next = None

        self.length -= 1
        return node
    
    def get(self, index):
        """
        Retrieves the node at the specified index.
        :param index: The index of the node to retrieve.
        :return: The node at the specified index or None if the index is out of bounds.
        :rtype: Node or None
        """
        if index < 0 or index >= self.length:
            return None

        if index < self.length / 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self.length -  index - 1):
                node = node.prev

        return node
    
    def set_value(self, index, value):
        """
        Sets the value of the node at the specified index.
        :param index: The index of the node to set the value for.
        :param value: The new value to set.
        :return: True if the value was set successfully, False if the index is out of bounds.
        :rtype: bool
        """
        node = self.get(index)
        if node:
            node.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index.
        :param index: The index at which to insert the new node.
        :param value: The value of the new node.
        """
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True

        node = Node(value)
        current = self.get(index)

        current.prev.next = node
        node.prev = current.prev
        node.next = current
        current.prev = node
        self.length += 1
        return True
    
    def remove(self, index):
        """
        Removes the node at the specified index.
        :param index: The index of the node to remove.
        :return: True if the node was removed successfully, False if the index is out of bounds.
        :rtype: bool
        """
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()

        node = self.get(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None

        self.length -= 1
        return node
    
    def is_palindrome(self):
        """        
        Checks if the list is a palindrome.
        :return: True if the list is a palindrome, False otherwise.
        :rtype: bool
        logic
        1. If the list is empty or has one element, it is a palindrome.
        2. Compare the first half of the list with the reversed second half.
        3. If all corresponding elements are equal, the list is a palindrome.
        4. If any pair of elements differ, the list is not a palindrome.
        5. Return True if all pairs match, otherwise return False.
        """
        if self.length <= 1:
            return True
            
        i = (self.length + 1) // 2
        start = self.head
        end = self.tail
        
        for _ in range(i):
            if start.value != end.value:
                return False
            
            start = start.next
            end = end.prev
            
        return True
    
    def reverse(self):
        """        
        Reverses the doubly linked list in place.
        This method swaps the head and tail, and reverses the next and prev pointers of each node.
        :return: None
        :rtype: None
        logic
        1. If the list is empty or has one element, no action is needed.
        2. Initialize pointers: prev as None, current as tail, and _next as tail.prev.
        3. Iterate through the list:
            a. Store the next node in _next.
            b. Set current's next to _next and prev to prev.
            c. Move prev to current and current to _next.
        4. After the loop, swap head and tail.
        5. The list is now reversed.
        :rtype: None
        """
        if self.length <= 1:
            return
        
        prev = None
        current = self.tail
        _next = self.tail.prev
        
        while current:
            _next = current.prev
            current.next = _next
            current.prev = prev
            
            prev = current
            current = _next
            
        self.head, self.tail = self.tail, self.head

    def partition_list(self, x):
        """
        #   +===================================================+
        #   |               WRITE YOUR CODE HERE                |
        #   | Description:                                      |
        #   | - Partitions a doubly linked list around a value  |
        #   |   `x`.                                            |
        #   | - All nodes with values less than `x` come before |
        #   |   nodes with values greater than or equal to `x`. |
        #   |                                                   |
        #   | Behavior:                                         |
        #   | - Uses two dummy nodes to create two sublists:    |
        #   |   one for nodes < x, and one for nodes >= x.      |
        #   | - Each node is added to the appropriate sublist   |
        #   |   while maintaining both next and prev pointers.  |
        #   | - The sublists are then joined together.          |
        #   | - The head of the list is updated to the start of |
        #   |   the merged result.                              |
        #   +===================================================+
        
        # if self.length <= 1:
        #     return
        
        # dummy_1 = Node(0)
        # dummy_2 = Node(0)
        
        # node_l = dummy_1
        # node_r = dummy_2
        # current = self.head
        
        # while current:
        #     if current.value < x:
        #         node_l.next = current
        #         current.prev = node_l
        #         node_l = current
        #     else:
        #         node_r.next = current
        #         current.prev = node_r
        #         node_r = current
                
        #     current = current.next

        # if dummy_1.next and dummy_2.next:    
        #     self.head = dummy_1.next
            
        #     node_l.next = dummy_2.next
        #     dummy_2.next.prev = node_l

        # self.head.prev = node_r.next = dummy_1.next = dummy_2.next = None

        :param x: The value around which to partition the list.
        :type x: int
        :return: None
        :rtype: None
        logic
        1. If the list is empty or has one element, no action is needed.
        2. Initialize two dummy nodes to create two sublists:
            - One for nodes with values less than `x`.
            - One for nodes with values greater than or equal to `x`.
        3. Traverse the list:
            a. If the current node's value is less than `x`, add it to the first sublist.
            b. If the current node's value is greater than or equal to `x`, add it to the second sublist.
            c. Maintain both next and prev pointers for each node.
        4. After traversing the list, connect the two sublists:
            a. Set the next pointer of the last node in the first sublist to the head of the second sublist.
            b. Set the prev pointer of the head of the second sublist to the last node of the first sublist if it exists.
        5. Update the head of the  list to the start of the merged result.
        6. Set the next pointer of the last node in the second sublist to None
        7. Set the prev pointer of the head of the list to None.
        """
        if not self.head:
            return None
    
        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head
    
        while current:
            if current.value < x:
                prev1.next = current
                current.prev = prev1
                prev1 = current
                
            else:
                prev2.next = current
                current.prev = prev2
                prev2 = current
            current = current.next
        
        prev1.next = dummy2.next
        if dummy2.next:
            dummy2.next.prev = prev1
        prev2.next = None
        
        self.head = dummy1.next
        self.head.prev = None

    def swap_pairs(self):
        """        
        Swaps every two adjacent nodes in the doubly linked list.
        :return: None
        :rtype: None
        logic
        1. If the list has less than two nodes, no action is needed.
        2. Initialize pointers:
            - pre_item as None (to track the previous node).
            - item_1 as the head (first node).
            - item_2 as the second node (head.next).
        3. Update the head to the second node (item_2).
        4. Iterate through the list:
            a. Store the next nodes:
                - next_item_1 as item_2.next (the node after item_2).
                - next_item_2 as next_item_1.next (the node after next_item_1).
            b. If next_item_1 exists, set next_item_2 to next_item
            c. If next_item_2 is None, set post_item to next_item_1.
            d. Set item_2's next to item_1 and prev to pre_item.
            e. Set item_1's next to post_item and prev to item_2.
            f. Update pre_item to item_1.
            g. Move item_1 and item_2 to the next pair of nodes.
        5. The list is now modified in place with every two adjacent nodes swapped.

        """
        
        if self.length < 2:
            return
        
        pre_item = None
        item_1 = self.head
        item_2 = self.head.next
        self.head = item_2
        
        while item_1 and item_2:
            next_item_1 = item_2.next
            if next_item_1:
                next_item_2 = next_item_1.next
            else:
                next_item_2 = None
                
            post_item = next_item_2 or next_item_1
            
            item_2.next = item_1
            item_2.prev = pre_item
            
            item_1.next = post_item
            item_1.prev = item_2
            
            pre_item = item_1
            item_1, item_2 = next_item_1, next_item_2

        # Best approach using dummy nodes
        # This is a more efficient way to swap pairs using dummy nodes.

        # if self.length < 2:
        #     return
    
        # dummy = Node(0)
        # dummy.next = self.head
        # self.head.prev = dummy
        
        # prev = dummy
        
        # while prev.next and prev.next.next:
        #     # Nodes to be swapped
        #     first = prev.next
        #     second = prev.next.next
            
        #     # Store next pair
        #     next_pair = second.next
            
        #     # Perform swap
        #     prev.next = second
        #     second.prev = prev
        #     second.next = first
        #     first.prev = second
        #     first.next = next_pair
            
        #     if next_pair:
        #         next_pair.prev = first
            
        #     # Move to next pair
        #     prev = first
        
        # # Update head
        # self.head = dummy.next
        # self.head.prev = None
        
        
if __name__ == "__main__":
    dll1 = DoublyLinkedList()
    # -------------------------------
    # Test Cases:
    # -------------------------------

    print("\nTest Case 1: Partition around 5")
    dll1.append(3)
    dll1.append(8)
    dll1.append(5)
    dll1.append(10)
    dll1.append(2)
    dll1.append(1)
    print("BEFORE: ", end="")
    dll1.print_list()
    dll1.partition_list(5)
    print("AFTER:  ", end="")
    dll1.print_list()

    print("\nTest Case 2: All nodes less than x")
    dll2 = DoublyLinkedList()
    dll2.append(1)
    dll2.append(2)
    dll2.append(3)
    print("BEFORE: ", end="")
    dll2.print_list()
    dll2.partition_list(5)
    print("AFTER:  ", end="")
    dll2.print_list()

    print("\nTest Case 3: All nodes greater than x")
    dll3 = DoublyLinkedList()
    dll3.append(6)
    dll3.append(7)
    dll3.append(8)
    print("BEFORE: ", end="")
    dll3.print_list()
    dll3.partition_list(5)
    print("AFTER:  ", end="")
    dll3.print_list()

    # print("\nTest Case 4: Empty list")
    # dll4 = DoublyLinkedList(1)
    # dll4.make_empty()
    # print("BEFORE: ", end="")
    # dll4.print_list()
    # dll4.partition_list(5)
    # print("AFTER:  ", end="")
    # dll4.print_list()

    print("\nTest Case 5: Single node")
    dll5 = DoublyLinkedList()
    dll5.append(1)
    print("BEFORE: ", end="")
    dll5.print_list()
    dll5.partition_list(5)
    print("AFTER:  ", end="")
    dll5.print_list()

    

    
