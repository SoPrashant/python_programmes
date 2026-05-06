
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
#
#
# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
# Example 3:
#
# Input: nums = [0,1,1,1,1,1,0,0,0]
# Output: 6
# Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.

#https://leetcode.com/problems/contiguous-array/description/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        total = 0
        i = -1
        length = 0
        d = {}
        d[total] = i

        for i in range(0, len(nums)):
            if nums[i] == 1:
                total += 1
            else:
                total -= 1

            if total in d:
                length = max(length, i - d[total])
            else:
                d[total] = i

        return length

