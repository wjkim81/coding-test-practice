from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, val: int):
        self.q.append(val)
        for i in range(len(self.q) - 1):
            val = self.q.popleft()
            self.q.append(val)

    def top(self):
        return self.q[0]
    
    def pop(self):
        return self.q.popleft()
    
    def empty(self):
        return not self.q