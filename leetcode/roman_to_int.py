class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(len(s)):
            if s[i] =="I":
                count+=1 
            elif s[i] =="V":
                if s[i-1]=="I":
                    count+= 3
                else:
                    count+= 5
            elif s[i]=="X":
                if s[i-1]=="I":
                    count+= 8
                else:
                    count+= 10

            elif s[i]=="L":
                if s[i-1]=="X":
                    count+= 30
                else:
                    count+= 50
            
            elif s[i]=="C":
                if s[i-1]=="X":
                    count+= 80
                else:
                    count+= 100
            elif s[i]=="D":
                if s[i-1]=="C":
                    count+= 300
                else:
                    count+= 500
            elif s[i]=="M":
                if s[i-1]=="C":
                    count+= 800
                else:
                    count+= 1000
        return count