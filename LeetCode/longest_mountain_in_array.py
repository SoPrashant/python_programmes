'''
https://leetcode.com/problems/longest-mountain-in-array/
'''

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        i = 1
        maxlen=0
        n = len(arr)

        while i < n-1:
            if arr[i-1] < arr[i] > arr[i+1]:  
                left = i - 1
                right = i + 1

                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1

                while right < n-1 and arr[right] > arr[right+1]:
                    right += 1  

                maxlen = max(maxlen,right-left+1)
                i = right        

            else:
                i += 1

        return maxlen    