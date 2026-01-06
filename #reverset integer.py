#reverset integer
#https://leetcode.com/problems/reverse-integer/description/

'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
'''




class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        num = ''

        if x < INT_MIN or x > INT_MAX:
            return 0
        else:
            if x<0:
                x = -x    
            while x>0:
                b=x%10
                x=x//10
                num += str(b)
                
            return int(num) 

                   

