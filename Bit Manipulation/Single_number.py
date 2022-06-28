"""
Solution to Leetcode #136. Single Number

Find an element that has only one occurrence in the list



- Approach 1: Use of set

Get the total sum of the list and the sum of all distinct elements in the list * 2
Then subtract between them, which gives the number that only appeared once in the list


- Approach 2: Use of XOR (bit manipulation)

Starting with 0, do XOR with each element in the list.
When there are elements that have already visited, these numbers will be "subtracted"
And the result of this XOR would represent the number of our interest
"""

def singleNumber1(nums: List[int]) -> int:
  double_sum = 0
  total_sum = 0
  visited = set()

  for num in nums:
      total_sum += num
      if num not in visited:
          visited.add(num)
          double_sum += num

  return double_sum * 2 - total_sum


def singleNumber2(nums: List[int]) -> int:
  xor = 0
  
  for num in nums:
    xor ^= num
  
  return xor
