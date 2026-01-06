#Sum Closest
#https://leetcode.com/problems/3sum-closest/description/

'''
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
'''

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]

                if abs(curr_sum - target) < abs(closest - target):
                    closest = curr_sum

                if curr_sum < target:
                    j += 1
                elif curr_sum > target:
                    k -= 1
                else:
                    return curr_sum #exact match

        return closest            







