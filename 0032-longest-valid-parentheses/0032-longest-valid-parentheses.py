# class Solution(object):
#     def longestValidParentheses(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         stack=[]
#         max_count=0
#         dict={"(":")"}
#         for ch in s:
#             if ch in dict:
#                 stack.append(ch)
#             elif stack and ch== dict [stack[-1]]:
                
#                     stack.pop()
#                     max_count+=2
            
#         return max_count
class Solution(object):
    def longestValidParentheses(self, s):
        stack = [-1]
        max_len = 0

        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len