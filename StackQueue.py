class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    A simple stack implementation using a linked list.
    """
    def __init__(self):
        self.top = None
        self.height = 0

    def print_stack(self):
        current = self.top
        stack_elements = []
        while current is not None:
            stack_elements.append(current.value)
            current = current.next
        print("Stack (top to bottom):", stack_elements)

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.height += 1

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = self.top.next
        node.next = None
        self.height -= 1
        return node

class Queue:
    """
    A simple queue implementation using a linked list.
    """
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def print_queue(self):
        current = self.first
        queue_elements = []
        while current is not None:
            queue_elements.append(current.value)
            current = current.next
        print("Queue (first to last):", queue_elements)
        
    def enqueue(self, value):
        node = Node(value)
        if self.last is None:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length += 1

    def dequeue(self):
        if self.first is None:
            return None
        node = self.first
        self.first = self.first.next
        if self.first is None:
            self.last = None
        node.next = None
        self.length -= 1
        return node






if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()  # Output: Stack (top to bottom): [30, 20, 10]
    
    print("Popped:", stack.pop())  # Output: Popped: 30
    stack.print_stack()  # Output: Stack (top to bottom): [20, 10]
    
    print("Popped:", stack.pop())  # Output: Popped: 20
    stack.print_stack()  # Output: Stack (top to bottom): [10]
    
    print("Popped:", stack.pop())  # Output: Popped: 10
    stack.print_stack()  # Output: Stack (top to bottom): []
