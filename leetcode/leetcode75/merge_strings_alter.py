class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        l1 = list(word1)
        l2 = list(word2)

        newWord = ""
        for i in range(max(len(l1),len(l2))):
            if i<len(l1):
                newWord+=l1[i]
            if i<len(l2):
                newWord+=l2[i]

        return newWord

s1 = Solution()
s1.mergeAlternately("abc","defghj")
