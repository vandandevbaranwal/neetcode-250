# Pattern: Monotonic Decreasing Stack
# Trigger: "nearest previous greater element" = maintain a decreasing stack

class StockSpanner:

    def __init__(self):
        # stack stores (price, span)
        self.stack = []

    def next(self, price: int) -> int:

        # today's stock always counts itself
        span = 1

        # merge spans of all previous prices <= current price
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()

        # push current price with its computed span
        self.stack.append((price, span))

        return span