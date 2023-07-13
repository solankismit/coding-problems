class Solution(object):
    def minimumCardPickup(self, cards):
        """
        :type cards: List[int]
        :rtype: int
        """
        # cards=[]
        min_num = -1
        dict={}
        if len(set(cards))==len(cards):
             return -1
        for i in range(len(cards)):
               if cards[i] in dict:
                    if min_num==-1 or min_num>i-dict[cards[i]]+1:
                         min_num = i - dict[cards[i]]+1
                    dict[cards[i]]=i
               else:
                    dict[cards[i]] = i
        # print(list(dict.values())) 
        return min_num
    

s1 = Solution()
# print(s1.minimumCardPickup([3,4,2,3,4,7]))
print(s1.minimumCardPickup([95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]))
# print(s1.minimumCardPickup([77,10,11,51,69,83,33,94,0,42,86,41,65,40,72,8,53,31,43,22,9,94,45,80,40,0,84,34,76,28,7,79,80,93,20,82,36,74,82,89,74,77,27,54,44,93,98,44,39,74,36,9,22,57,70,98,19,68,33,68,49,86,20,50,43]))