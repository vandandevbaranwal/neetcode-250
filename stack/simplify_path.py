# Pattern: Stack + String Parsing
# Trigger: "simplify Unix file path" = process each directory using a stack

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        # add an extra '/' to process the last directory
        for c in path + "/":

            if c == "/":

                # ".." means go to parent directory
                if cur == "..":
                    if stack:
                        stack.pop()

                # ignore "" and "."
                elif cur != "" and cur != ".":
                    stack.append(cur)

                # start reading the next directory name
                cur = ""

            else:
                cur += c

        # rebuild the canonical path
        return "/" + "/".join(stack)