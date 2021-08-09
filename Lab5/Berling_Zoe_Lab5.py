from collections import deque

"""Zoe Berling Algorithms Lab 5 Stack and QueueADTs"""
"""You are to create two Python classes, MyStack and MyQueue. These should provide a stack and queue implementation, respectively"""

class MyStack():
    """Use standard python list as underlying data structure"""
    def __init__(self):
        self.mystack = []

    def push(self, int):
        """Add to end of stack"""
        return self.mystack.append(int)

    def pop(self):
        """Remove from end of stack"""
        if not self.empty():
            return self.mystack.pop()
        else:
            return "Error: Can't pop element from empty stack."

    def empty(self):
        """Return True if empty: Return False if not empty"""
        if len(self.mystack) > 0:
            return False
        else:
            return True

    def top(self):
        """peek at first element in the stack without removing it"""
        return self.mystack[0]

    def show(self):
        print(self.mystack)

# Testing code for stack

s = MyStack()
print(s.empty())
s.push(5)
s.push(8)
print(s.pop())
s.push(3)
print(s.empty())
print(s.top())
print(s.pop())
print(s.pop())
print(s.pop())

class MyQueue():
    def __init__(self):
        """Create an empty queue using deque from collections"""
        self.myqueue = deque([])

    def enqueue(self, int):
        """Add to end of queue"""
        return self.myqueue.append(int)

    def dequeue(self):
        """Remove from front of queue"""
        if not self.empty():
            return self.myqueue.popleft()
        else:
            return "Error: Can't dequeue element from empty queue"

    def front(self):
        """Check first item of queue without removing it"""
        return self.myqueue[0]

    def empty(self):
        """Return True if empty: Return False if not empty"""
        if self.myqueue:
            return False
        else:
            return True

    def show(self):
        """Show queue"""
        print(self.myqueue)

# Testing code for Queue
q = MyQueue()
print(q.empty())
q.enqueue(5)
q.enqueue(8)
print(q.dequeue())
q.enqueue(3)
print(q.empty())
print(q.front())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

