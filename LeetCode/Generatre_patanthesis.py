'''
22. Generate Parentheses
Solved
Medium

Topics
premium lock icon
Companies
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
'''


#https://leetcode.com/problems/generate-parentheses/description/


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s, open, close):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open < n:
                backtrack(s + "(", open+1, close)

            if close < open:
                backtrack(s + ")", open, close+1)

        backtrack("", 0, 0)
        return res

