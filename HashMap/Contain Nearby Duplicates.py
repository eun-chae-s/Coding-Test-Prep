"""
Leetcode #219 Contain Duplicates II

Approach: Use of Hash Map
- create a hash map that keeps track of the recent index for each element
"""
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
  count = {}
  n = len(nums)

  for i in range(n):
      if nums[i] not in count:
          count[nums[i]] = i
      else:
          j = count[nums[i]]
          if abs(i - j) <= k:
              return True

          count[nums[i]] = i

  return False
