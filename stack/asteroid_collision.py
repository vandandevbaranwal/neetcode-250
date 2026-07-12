# Pattern: Monotonic Stack / Collision Simulation
# Trigger: "objects collide in sequence" = use a stack to keep surviving objects

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:

            # collision occurs only when:
            # stack top moves right (+)
            # current asteroid moves left (-)
            while stack and a < 0 and stack[-1] > 0:

                diff = a + stack[-1]

                # current asteroid is larger
                if diff < 0:
                    stack.pop()

                # stack asteroid is larger
                elif diff > 0:
                    a = 0

                # both explode
                else:
                    a = 0
                    stack.pop()

            # asteroid survives
            if a:
                stack.append(a)

        return stack