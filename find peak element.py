
#162. Find peak element
#852. Peak Index in a Mountain Array
#https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
#https://leetcode.com/problems/find-peak-element/description/

'''

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
'''



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
       low = 0
       high = len(nums)-1

       while low < high:
        mid = (low+high)//2
        if nums[mid] < nums[mid+1]:
            low = mid+1
        else:
            high = mid
        
       return low 

