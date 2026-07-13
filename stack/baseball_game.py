# Pattern: Stack Simulation
# Trigger: "perform operations based on previous values" = use a stack to maintain history

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:

            # sum of previous two scores
            if op == "+":
                stack.append(stack[-1] + stack[-2])

            # double previous score
            elif op == "D":
                stack.append(2 * stack[-1])

            # invalidate previous score
            elif op == "C":
                stack.pop()

            # numeric score
            else:
                stack.append(int(op))

        return sum(stack)