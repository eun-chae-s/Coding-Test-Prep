"""
Leetcode Q16. 3Sum Closest

3Sum 문제의 기출변형!
"""
import math


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # 1. sort the nums
        nums.sort()

        # 2. declare n and result
        n = len(nums)
        result = math.inf

        # 3. iterate through the nums
        for i in range(n):
            # skip the duplicated numbers to reduce the time complexity
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 4. iterate through the rest of nums
            s, e = i + 1, n - 1
            while s < e:
                num = nums[s] + nums[i] + nums[e]
                if num == target:
                    return num

                if abs(target - num) <= abs(target - result):
                    result = num

                if num > target:
                    e -= 1
                # 더하는 수를 더 크게 만듦으로써 타겟으로부터의 차이를 줄인다...!
                else:
                    s += 1

        return result
