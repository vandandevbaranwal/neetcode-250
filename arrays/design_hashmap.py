# Pattern: Direct Address Table
# Trigger: "keys are in a small fixed range" = use array indexing instead of hashing

class MyHashMap:

    def __init__(self):
        # initialize every key as not present
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        # store value directly at index = key
        self.map[key] = value

    def get(self, key: int) -> int:
        # return stored value (-1 if absent)
        return self.map[key]

    def remove(self, key: int) -> None:
        # mark key as removed
        self.map[key] = -1