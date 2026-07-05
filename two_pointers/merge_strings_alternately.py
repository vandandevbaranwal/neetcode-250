# Pattern: Two Pointers
# Trigger: "merge two sequences alternately" = traverse both with independent pointers

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n, m = len(word1), len(word2)

        res = []

        i = j = 0

        # continue until both strings are fully processed
        while i < n or j < m:

            # add next character from word1
            if i < n:
                res.append(word1[i])

            # add next character from word2
            if j < m:
                res.append(word2[j])

            i += 1
            j += 1

        return "".join(res)