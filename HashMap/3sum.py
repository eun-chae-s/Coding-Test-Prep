"""
Leetcode #15. 3Sum

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Solution adapted from the discussion board
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """

        :param nums: list of integers
        :return:
        """
        # sort the list
        nums.sort()

        # declare variables
        n = len(nums)
        result = []

        # iterate through nums (time complexity: n^2)
        for i in range(n):
            # skip if the current value is same as the previous one (already found the solution!)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # find the target (reduced to 2Sum problem)
            target = (-1) * nums[i]

            # assign the two pointers (tracking of the complements)
            p1 = i + 1
            p2 = n - 1

            while p1 < p2:
                if nums[p1] + nums[p2] == target:
                    result.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    while p1 < p2 and nums[p1 - 1] == nums[p1]:
                        p1 += 1
                elif nums[p1] + nums[p2] < target:
                    p1 += 1
                else:
                    p2 -= 1

        return result
