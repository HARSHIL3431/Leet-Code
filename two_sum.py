# LeetCode: Two Sum
# Difficulty: Easy
# Pattern: Hash Map
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need], i]
            seen[num] = i
