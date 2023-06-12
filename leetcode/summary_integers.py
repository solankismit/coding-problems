"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""

class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i = []
        ans = []
        for j in nums:
            # print(j)
            # print("H-->"+str(i[len(i)-1]+1)) if len(i)>1 else None
            if i == []:
                i.append(j)
            elif (i[len(i)-1]+1) == j:
                i.append(j)
            else:
                if len(i)==1:
                    ans.append(str(i[0]))
                else:
                    ans.append(str(i[0])+"->"+str(i[len(i)-1]))
                i=[]
                i.append(j)
        if len(i)==1:
                    ans.append(str(i[0]))
        elif len(i)>0:
                    ans.append(str(i[0])+"->"+str(i[len(i)-1]))
        return ans
        # print(ans)


s1 = Solution()
print(s1.summaryRanges([0,1,2,4,5,7]))