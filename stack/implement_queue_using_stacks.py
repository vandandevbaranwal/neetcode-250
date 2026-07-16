# Pattern: Stack Simulation
# Trigger: "implement a queue using stacks" = use two stacks to reverse order

class MyQueue:

    def __init__(self):
        # stack1 stores incoming elements
        # stack2 is used temporarily during pop/peek
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        # enqueue element
        self.stack1.append(x)

    def pop(self) -> int:
        # move all except the oldest element
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        # oldest element = front of queue
        res = self.stack1.pop()

        # restore original order
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return res

    def peek(self) -> int:
        # move all except the oldest element
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())

        # oldest element
        res = self.stack1[-1]

        # restore original order
        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return res

    def empty(self) -> bool:
        return not self.stack1