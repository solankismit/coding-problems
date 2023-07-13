"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         output = [1]
#         for i in range(1,len(nums)):
#             output.append(output[i-1]*nums[i-1])
#             for j in range(i):
#                 output[j] *=nums[i]
#         return output
class Solution:
    def productExceptSelf(self, nums):
        l=len(nums)
        left, right = [1] * l, [1] * l
        for i in range(1, l):
            left[i] *= left[i-1]*nums[i-1]
            right[-i-1] *= right[-i]*nums[-i]
        return [lv*rv for lv, rv in zip(left, right)]
    

s1 = Solution()
arr =[]
print(s1.productExceptSelf(arr))
