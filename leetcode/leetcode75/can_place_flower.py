"""

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = list(flowerbed)
        adjecent_zeros = []
        temp = 0
        prev = -1
        curr = -1
        for idx, i in enumerate(flowerbed):
            curr = i
            if prev == -1:
                prev = i
            if curr == prev == 0:
                temp += 1
                # print(temp)
            if (curr == 1 or idx == len(flowerbed) - 1) and temp > 0:
                print(temp)
                if curr == 1:
                    adjecent_zeros.append(temp - 1)
                else:
                    adjecent_zeros.append(temp)
                temp = 0
            prev = curr
        print(adjecent_zeros)
        zeros = list(map(lambda x: x % 2 + int(x / 2), adjecent_zeros))
        return sum(zeros) >= n


S1 = Solution()
S1.canPlaceFlowers([0, 0, 1, 0, 1], 2)
