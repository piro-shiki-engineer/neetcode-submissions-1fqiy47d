class MinStack:
    """
    Monotnically Decreasing stack

    We can solve by using two stakc
    """
    def __init__(self):
        self.stack = []
        self.min_val = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_val:
            self.min_val.append(min(self.min_val[-1], val))
        else:
            self.min_val.append(val)

    def pop(self) -> None:
        self.min_val.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]
