# Pattern: Queue Simulation
# Trigger: "implement a stack using queues" = rotate the queue after each push

from collections import deque

class MyStack:

    def __init__(self):
        # use one queue to simulate a stack
        self.q = deque()

    def push(self, x: int) -> None:
        # add new element to the back
        self.q.append(x)

        # rotate previous elements behind the new element
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # front of queue represents stack top
        return self.q.popleft()

    def top(self) -> int:
        # peek at stack top
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0