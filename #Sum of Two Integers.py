#Sum of Two Integers

'''
371.
Given two integers a and b, return the sum of the two integers without using the operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
'''

class Solution:

    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF # 32 bits of 1s -> 4294967295
        MAX_INT = 0x7FFFFFFF # max signed 32-bit -> 2147483647
        a = a & MASK # verifying integer
        b = b & MASK # verifying integer
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK

        return a if a <= MAX_INT else ~(a ^ MASK)    
