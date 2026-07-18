# Pattern: Stack + String Parsing
# Trigger: "nested encoded strings" = use a stack to decode from the innermost level

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:

            # push everything until we find a closing bracket
            if ch != "]":
                stack.append(ch)

            else:
                # build the encoded substring
                substr = ""

                while stack[-1] != "[":
                    substr = stack.pop() + substr

                # remove '['
                stack.pop()

                # extract the repetition count
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # push decoded substring back
                stack.append(int(k) * substr)

        return "".join(stack)