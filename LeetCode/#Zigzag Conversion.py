#Zigzag Conversion
#https://leetcode.com/problems/zigzag-conversion/description/

'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
'''




class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row = {i:"" for i in range(numRows)}
        cur, step = 0, 1 #zigzag pattern

        if numRows < 2:
            return s

        for ch in s:
            row[cur] += ch
            if cur == 0:  #zigzag pattern
                step = 1
            elif cur == numRows - 1:
                step = -1
            cur += step    

        return(''.join([values for values in row.values()]))        
        




