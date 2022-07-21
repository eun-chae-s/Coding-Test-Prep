"""
Leetcode: First Missing Positive
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        minimum = nums[0]
        maximum = nums[0]
        data = {nums[0]: True}
        
        for i in range(1, len(nums)):
            element = nums[i]
            if element < minimum and element > 0:
                minimum = element
            if element > maximum and element > 0:
                maximum = element
            
            data[element] = True
        
        if minimum > 1:
            return 1
        
        for i in range(minimum, maximum):
            if i not in data and i > 0:
                return i
        
        if maximum <= 0:
            return 1
        else:
            return maximum + 1
