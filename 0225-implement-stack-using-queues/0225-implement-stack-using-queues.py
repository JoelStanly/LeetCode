class MyStack:

    def __init__(self):
        self.val = []
        

    def push(self, x: int) -> None:
        self.val.append(x)

    def pop(self) -> int:
        return self.val.pop()

    def top(self) -> int:
        return self.val[-1]

    def empty(self) -> bool:
        return len(self.val) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()