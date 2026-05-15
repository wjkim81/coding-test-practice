class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int):
        self.stack1.append(val)

    def _move(self):
        if not self.stack2:
            while self.stack1:
                val = self.stack1.pop()
                self.stack2.append(val)

    def pop(self):
        self._move()
        return self.stack2.pop()
    
    def peek(self):
        self._move()
        return self.stack2[-1]
    
    def empty(self):
        return not self.stack1 and not self.stack2



    