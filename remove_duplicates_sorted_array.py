# LeetCode: Remove Duplicates from Sorted Array
# Difficulty: Easy
# Pattern: Two Pointers
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1  # index for unique elements

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k
