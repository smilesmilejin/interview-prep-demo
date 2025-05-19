"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input will have at most one solution, and you may not use the same element twice.

Return the answer in a list with the smaller index first.

If there is no pair that adds together to the target, return an empty list.

Example: 
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Adapted from: https://leetcode.com/problems/two-sum/

"""

def two_sum(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return []


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([5, 7, 3, 15], 22) == [1, 3]
assert two_sum([1, 2], 3) == [0, 1]
assert two_sum([5, 4, 6], 22) == []
assert two_sum([5, -15, 6], -10) == [0, 1]
print("All tests passed!")