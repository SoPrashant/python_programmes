#Maximum Sum Circular Subarray

'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

 

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

Hint : Kadane's algorithm
'''
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currentmax = nums[0]
        currentmin = nums[0]
        maxsum = minsum = nums[0]
        total = nums[0]
        for x in nums[1:]:
            currentmax = max(x, currentmax+x)
            maxsum = max(maxsum, currentmax)
            currentmin = min(x, currentmin+x)
            minsum = min(minsum, currentmin)
            
            total += x

        if maxsum<0:
            return maxsum    

        return max(maxsum, total-minsum)

obj = Solution()
nums = list(map(int, input().split()))
print(obj.maxSubarraySumCircular(nums))