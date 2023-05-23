class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        items={}
        nums = list(nums)
        for num in nums:
            if items.keys().__contains__(num):
                items[num] +=1
            else:
                items[num] = 1
        freq_items = []
        items = sorted(items.items(),key=lambda x:x[1],reverse=True)
        while(k>0):
            k-=1
            freq_items.append(items[k][0])
        return freq_items
sol = Solution()
sol.topKFrequent([1,1,1,2,2,3,4],2)