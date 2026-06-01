class MinStack:

    def __init__(self):
        self.stack = []
        self.ministack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ministack or val <= self.ministack[-1]:
            self.ministack.append(val)
        

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.ministack[-1]:
            self.ministack.pop()
        return popped

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ministack[-1]
        
