"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        count = {}
        pos = -1
        for index, letter in enumerate(s):
            if letter in count and count[letter] > pos:
                pos = count[letter]
            count[letter] = index
            output = max(output,index-pos)
        return output