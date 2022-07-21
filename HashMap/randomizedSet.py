"""
Leetcode: Create a Randomized Set class

- Use of Hashmap and Array
"""
import random

class RandomizedSet:
    
    def __init__(self):
        self.storage = {}
        self.data_list = []
        
    def insert(self, val: int) -> bool:
        if val not in self.storage:
            self.data_list.append(val)
            self.storage[val] = len(self.data_list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.storage:
            return False
        
        index = self.storage[val]
        replaced = self.data_list[-1]
        
        self.data_list[index] = replaced
        self.storage[replaced] = index
        self.data_list[-1] = val
        self.data_list.pop()
        
        self.storage.pop(val)
        return True
        
    def getRandom(self) -> int:
        return random.choice(self.data_list)
