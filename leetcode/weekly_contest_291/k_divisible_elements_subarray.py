"""Given an integer array nums and two integers k and p, return the number of distinct subarrays which have at most k elements divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:

They are of different lengths, or
There exists at least one index i where nums1[i] != nums2[i].
A subarray is defined as a non-empty contiguous sequence of elements in an array."""

class Solution(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        subarrays = set()
        tmpArr = ""
        tmpk = k
        for j in range(len(nums)):
            for i in range(j,len(nums)):
                print(subarrays)
                tmpArr+=str(nums[i])+','
                # print(tmpArr)
                if nums[i] % p ==0: tmpk-=1
                if tmpk>=0 :
                    # print(subarrays)
                    subarrays.add(tmpArr)
                if tmpk==-1:
                    tmpArr=""
                    tmpk=k
            if tmpArr!="":
                subarrays.add(tmpArr)
            tmpk = k
            tmpArr=""
        # print(subarrays)
        print(len(subarrays))
        return len(subarrays)

s1 = Solution()
s1.countDistinct([2,3,3,2,2],2,2)
# s1.countDistinct([10,2,17,7,20],1,10)

# arr = [15,36,58,72,23,71,73,48,43,17,67,90,76,96,4,68,19,33,55,51,37,23,98,46,65,88,5,4,78,10,100,1,18,8,96,98,81,22,12,3,55,38,69,96,32,38,16,11,12,51,93,91,72,16,43,48,69,38,10,91,99,57,67,19,13,12,80,27,96,11,86,33,51,33,12,37,42,33,47,17,6,4,54,32,41,81,24,88,65,1,71,100,5,96,10,87,89,44,86,86,40,60,97,27,91,14,63,94,35,41,38,46,33,91,49,86,65,26,56,3,6,30,54,78,23,34,4,56,20,52,92,74,39,22,27,51,92,41,38,71,9,40,16,53,28,86,95,94,33,59,100,39,34,79,84,92,66,69,28,32,83,5,89,14,8,49,52,78,11,30,45,94,92,93,44,26,76,72,62,17,3,3,50]
# k=54
# p=67

arr = [80,42,52,49,66,44,18,48,77,12,56,63,24,36,70,36,81,44,35,24,72,43,48,3,49,67,89,36,100,63,52,56,71,10,61,24,14,5,20,39,1,74,28,73,77,39,44,62,39,38,77,3,98,43,62,70,50,22,95,57,99,72,47,26,49,95,5,93,100,11,2,68,65,96,58,14,99,28,63,59,84,37,65,81,93,4,30,91,40,11,56,77,85,18,52,60,86,87,24,86,51,84,100,10,82,32,18,50,49,10,47,56,20,3,55,4,51,26,42,96,10,78,99,53,100,25,95,4,43,70,2,41,57,62,21,17,39,45,100,14,77,56,48,73,64,42,8,53,24]
k = 134
p = 61
# s1.countDistinct(arr,k,p)