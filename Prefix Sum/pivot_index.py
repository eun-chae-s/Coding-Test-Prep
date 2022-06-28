"""
Solutions to Leetcode #724. Find the pivot index

Approach 1:
- get the array that has an accumlative sum from left
- get another array that has an accumulative sum from right
- iterate from 0 to len(arr) and check if the left[i - 1] and right[i + 1] are equal

Approach 2:
- keep track of an accumulative sum from the left
- for each item in list, check if accumulative sum * 2 + item is equal to the total sum of list
- if it is, then return that index
- otherwise, add item to accumulative sum
"""
def pivotIndex1(nums: List[int]) -> int:
  n = len(nums)
  left_sum = [0] * n
  right_sum = [0] * n

  for i in range(n):
      if i == 0:
          left_sum[i] = nums[i]
      else:
          left_sum[i] = left_sum[i - 1] + nums[i]

  for i in range(n - 1, -1, -1):
      if i == n - 1:
          right_sum[i] = nums[i]
      else:
          right_sum[i] = nums[i] + right_sum[i + 1]

  for i in range(n):
      if i == 0:
          if n == 1 or (n > 1 and right_sum[1] == 0):
              return 0
      elif i == n - 1:
          if left_sum[n - 2] == 0:
              return n - 1
      else:
          if left_sum[i - 1] == right_sum[i + 1]:
              return i

  return -1

def pivotIndex2 (nums: List[int]) -> int:
  n = len(nums)
  sum_from_left = 0
  total_sum = sum(nums)

  for i in range(n):
      if sum_from_left * 2 + nums[i] == total_sum:
          return i
      else:
          sum_from_left += nums[i]

  return -1
  
