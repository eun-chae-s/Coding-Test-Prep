"""
Sort an Array in ascending order
"""
import math

class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # unsorted => heap
        heap = self._toHeap(nums)

        # heap => sorted
        sorted_arr = self._toSorted(heap)

        return sorted_arr


    def _toHeap(self, nums: list[int]) -> list[int]:
        n = len(nums)
        start = n - 1 - math.ceil(n / 2)

        for i in range(start, -1, -1):
            left = 2 * i + 1
            right = 2 * i + 2
            j = i

            while right < n:
                if nums[left] < nums[right]:
                    larger = right
                else:
                    larger = left

                if nums[j] < nums[larger]:
                    nums[j], nums[larger] = nums[larger], nums[j]
                    j = larger
                    left, right = 2 * j, 2 * j + 1
                else:
                    break

        return nums

    def _toSorted(self, nums: list[int]) -> list[int]:
        curr = len(nums) - 1
        pt = 0

        while curr > 1:
            nums[pt], nums[curr] = nums[curr], nums[pt]

            left, right = 1, 2

            while right < curr:
                if nums[left] < nums[right]:
                    larger = right
                else:
                    larger = left

                if nums[pt] < nums[larger]:
                    nums[pt], nums[larger] = nums[larger], nums[pt]
                    pt = larger
                    left, right = 2 * pt + 1, 2 * pt + 2
                else:
                    break

            pt = 0
            curr = curr - 1

        if nums[0] > nums[1]:
            nums[0], nums[1] = nums[1], nums[0]

        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 1, 1, 2, 0, 0]
    result = solution.sortArray(nums)
    print(result)
