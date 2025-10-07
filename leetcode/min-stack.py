class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if not self.min_val:
            m = val
        else:
            m = min(val, self.min_val[-1])
        self.min_val.append(m)

    def pop(self) -> None:
        self.min_stack.pop()
        self.min_val.pop()        

    def top(self) -> int:
        return self.min_stack[-1]     

    def getMin(self) -> int:
        if self.min_val:
            return self.min_val[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()