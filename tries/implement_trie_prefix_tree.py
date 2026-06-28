# Pattern: Trie (Prefix Tree)
# Trigger: "insert/search/prefix queries on strings" = Trie

class TrieNode:
    def __init__(self):
        self.children = {}          # maps character -> TrieNode
        self.is_end_of_word = False # marks end of a complete word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        # create nodes for characters if they don't exist
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        # mark the last node as the end of a word
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root

        # traverse the trie
        for char in word:
            if char not in node.children:
                return False

            node = node.children[char]

        # word exists only if end-of-word marker is set
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        # verify every character of the prefix exists
        for char in prefix:
            if char not in node.children:
                return False

            node = node.children[char]

        return True