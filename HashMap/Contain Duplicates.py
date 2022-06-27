"""
Idea for Leetcode #217 and #219 Contain Duplicates

## Leetcode #217

### Approach 1: Use of Hashmap
- create a hash map variable that stores the number of occurrences of each element in the given array
- do linear iteration
- if a particular element is already in the hash map, return true
- otherwise, iterate rest of array
- As long as there is no early return, this means that every element in the array is distinct

### Approach 2: Use of the difference between set and list
- set is a data type that does not contain duplicates
- so we create a new set variable that contains distinct element from the given array
- compare the length of set and length of list
- return true if the lengths are different
- otherwise, return false
"""

def containsDuplicate1(nums: List[int]) -> bool:
  count = {}

  for num in nums:
      if num not in count:
          count[num] = 1
      else:
          return True

  return False

def containsDuplicate2(self, nums: List[int]) -> bool:
  nums_set = set()
        
  for num in nums:
      nums_set.add(num)

  return len(nums_set) != len(nums)
