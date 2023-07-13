class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        triples = []
        # prev = nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i]>prev:
        #         triples +=1
        #         if triples == 3: return True
        #     else:
        #         triples = 1
        #     prev = nums[i]
        # return False
        first = second = float('inf') 
        for n in nums: 
            if n <= first: 
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False

            


s1 = Solution()
s1.increasingTriplet([20,100,10,12,5,13])