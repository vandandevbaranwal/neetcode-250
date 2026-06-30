# Pattern: Design Data Structure (Hash Set)
# Trigger: "support add, remove, contains operations" = Hash Set

class MyHashSet:

    def __init__(self):
        # store unique elements
        self.data = []

    def add(self, key: int) -> None:
        # insert only if key doesn't already exist
        if key not in self.data:
            self.data.append(key)

    def remove(self, key: int) -> None:
        # remove key if present
        if key in self.data:
            self.data.remove(key)

    def contains(self, key: int) -> bool:
        # membership check
        return key in self.data