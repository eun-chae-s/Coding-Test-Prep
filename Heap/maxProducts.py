import math


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return (nums[0] - 1) * (nums[1] - 1)

        # unsorted => heap
        heap = self._toHeap(nums)
        print(heap)

        # take index 0 * max(index 1, index 2 values)
        return (heap[0] - 1) * (max(heap[1], heap[2]) - 1)

    def _toHeap(self, nums: list[int]) -> list[int]:
        n = len(nums)
        start = n - 1 - math.ceil(n / 2)

        for i in range(start, -1, -1):
            print(i)
            print(nums)
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
                    left, right = 2 * j + 1, 2 * j + 2
                else:
                    break

        return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 5, 4, 5]
    result = solution.maxProduct(nums)
    print(result)
