#singleNumber

'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]

Output: 1

Example 2:

Input: nums = [4,1,2,1,2]

Output: 4

https://leetcode.com/problems/single-number/description/

'''
from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x,y: x^y, nums)
    

nums = list(map(int, input().split()))
result=Solution()
ans = result.singleNumber(nums)

print(ans)