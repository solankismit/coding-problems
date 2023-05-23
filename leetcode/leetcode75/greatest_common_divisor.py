class Solution:
    def gcdOfStrings(self, str1, str2):

        def check(s, s1):

            n = len(s)
            m = len(s1)

            if n % m != 0:

                return False

            else:

                c = ""
                v = n // m

                for i in range(0, v):
                    c += s1

            return c == s

        i = 0
        j = 0
        n = len(str1)
        m = len(str2)

        s = ""
        while i < n and j < m:

            if str1[i] == str2[j]:

                i += 1
                j += 1

                gcd = str1[:i]

                if check(str1, gcd) and check(str2, gcd):
                    s = gcd
            else:

                break

        return s


