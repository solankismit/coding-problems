# """
# The appeal of a string is the number of distinct characters found in the string.

# For example, the appeal of "abbca" is 3 because it has 3 distinct characters: 'a', 'b', and 'c'.
# Given a string s, return the total appeal of all of its substrings.

# A substring is a contiguous sequence of characters within a string.
# """
# class Solution(object):
#     def appealSum(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         s = "abbca"
#         tmps = list(s)
#         print(tmps)
#         prevj = 0
#         count = 0
#         for i in range(len(tmps)):
#             for j in range(0,len(tmps),i+1):
#                 print(j,end = " ")
#                 count +=len(set(list(tmps[prevj:j+1])))
#                 prevj = j
#             print()
#         print(count)
# s1 = Solution()
# s1.appealSum("abbca")        

x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "hello1", "x should be 'hello'"

