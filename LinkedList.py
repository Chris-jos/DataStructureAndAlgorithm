from NodeConstructor import Node


class LinkedList:
    """
    LinkedList class
    """
    def __init__(self, value):
        """
        Initialise LinkedList
        param value: Initial node value
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

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
        Method to append (add to the end) an element to LinkedList
        param value: Node value
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True

    def pop(self):
        """
        Method to pop (remove from the end) an element from LinkedList 
        """
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        """
        Method to prepend (add to the begining) an element to LinkedList 
        param value: Node value
        """
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1
        return True

    def pop_first(self):
        """
        Method to pop first element from LinkedList
        """
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None

        self.length -= 1
        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        """
        Method to get LL node at the specified index
        param index: LinkedList Index
        """
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        
        return temp
    
    def set_value(self, index, value):
        """
        Method to update LL node value at the specified index
        param index: LinkedList Index
        param value: value to update
        """
        temp = self.get(index)

        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        """
        Method to insert a new LL node at the specified index
        param index: LinkedList Index
        param value: node value to insert
        """
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        temp = self.get(index-1)

        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

        return True
    
    def remove(self, index):
        """
        Method to remove a LL node at the specified index
        param index: LinkedList Index
        """
        if index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        
        prev = self.get(index-1)
        temp = prev.next

        prev.next = temp.next
        temp.next = None
        self.length -= 1

        return temp
    
    def reverse(self):
        """
        Method to reverse LinkedList
        """
        temp = self.head
        self.head =  self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        return True
