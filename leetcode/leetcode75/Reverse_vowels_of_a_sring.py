"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        listString = list(s)
        vowels = ['a','A','e','i','o','E','I','O','U','u']
        i = 0
        j=len(listString)-1
        while i<j:
            while (listString[i] not in vowels) and i < j:
                # print(i,j)
                i+=1
            while (listString[j] not in vowels) and j>i:
                # print(i,j)
                j-=1
            if i>j: break
            listString[i],listString[j] = listString[j],listString[i]
            i+=1
            j-=1
            # print(listString)
        # print(listString)
        s = ''.join(listString)
        return s

s1 = Solution()
print(s1.reverseVowels('leetcode') )           
        
        