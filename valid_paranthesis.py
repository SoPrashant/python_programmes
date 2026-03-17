'''
#https://leetcode.com/problems/valid-parentheses/description/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false



Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''


class Solution:
    '''
    # my approach

    def isValid(self, s: str) -> bool:
        stack = []
        mapping={')':'(','}':'{',']':'['}


        for i in s:
            if i in list(mapping.values()):
                stack.append(i)
            elif i in mapping:
                if len(stack) > 0 and mapping.get(i) == stack[-1]:
                    stack.pop()
                else:
                    return False
        print(stack)
        if len(stack) == 0:
            return True
        return False
    '''

    # optimum approach
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in mapping:
                if not stack or stack.pop() != mapping[i]:
                    return False
            else:
                stack.append(i)

        return not stack


