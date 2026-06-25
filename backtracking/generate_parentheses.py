# Pattern: Backtracking with Constraints
# Trigger: "generate all valid combinations" = build incrementally while maintaining validity

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):

            # valid parentheses string completed
            if openN == closedN == n:
                res.append("".join(stack))
                return

            # choose '(' if we still have some left
            if openN < n:
                stack.append("(")

                # explore
                backtrack(openN + 1, closedN)

                # undo
                stack.pop()

            # choose ')' only if it keeps the string valid
            if closedN < openN:
                stack.append(")")

                # explore
                backtrack(openN, closedN + 1)

                # undo
                stack.pop()

        backtrack(0, 0)

        return res