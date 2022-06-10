"""
Leetcode #18 4Sum
"""
class Solution:
    def threeSum(self, nums: list[int], target: int) -> list[list[int]]:
        # declare variables
        n = len(nums)
        result = []

        # iterate through nums (time complexity: n^2)
        for i in range(n):
            # skip if the current value is same as the previous one (already found the solution!)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # find the target (reduced to 2Sum problem)
            target2 = target - nums[i]

            # assign the two pointers (tracking of the complements)
            p1 = i + 1
            p2 = n - 1

            while p1 < p2:
                if nums[p1] + nums[p2] == target2:
                    result.append([nums[i], nums[p1], nums[p2]])
                    p1 += 1
                    while p1 < p2 and nums[p1 - 1] == nums[p1]:
                        p1 += 1
                elif nums[p1] + nums[p2] < target2:
                    p1 += 1
                else:
                    p2 -= 1

        return result

    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        # step 1. sorting
        nums.sort()

        # step 2. declare some variables
        n = len(nums)
        result = []

        # step 3. iterate through the list
        for i in range(n):
            # step 4. check if it is duplicated letter
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # step 5. find the complement value (reduced to 3Sum)
            comp = target - nums[i]
            r = self.threeSum(nums[i + 1:], comp)

            for lst in r:
                result.append([nums[i]] + lst)

        return result
