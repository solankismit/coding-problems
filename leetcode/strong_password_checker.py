"""
A password is considered strong if the below conditions are all met:

It has at least 6 characters and at most 20 characters.
It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
It does not contain three repeating characters in a row (i.e., "Baaabb0" is weak, but "Baaba0" is strong).
Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

In one step, you can:

Insert one character to password,
Delete one character from password, or
Replace one character of password with another character.
 

Example 1:

Input: password = "a"
Output: 5
Example 2:

Input: password = "aA1"
Output: 3
Example 3:

Input: password = "1337C0d3"
Output: 0

"""
class Solution(object):
    steps=0
    def strongPasswordChecker(self, password): 

        """
        :type password: str
        :rtype: int
        """
        def checkConsecutive(password):
            count = 1
            for i in range(1, len(password)):
                if password[i] == password[i-1]:
                    count += 1
                    if count == 3:
                        return True
                else:
                    count = 1
            return False
        def stepsRequiredMakeConsecutiveStrong(password):
            count = 0
            steps=0
            if len(password) > 1:
                for i in range(1, len(password)):
                    print(password)
                    if i+1 < len(password) and password[i] == password[i-1] :
                        count += 1
                        if count == 3:
                            count = 0
                            steps += 1  
                            password = password[:i-2] + password[i+1:]
                            # print(password)
            # return password
            return steps
        
        def checkLowercase(password):
            for i in password:
                if i.islower():
                    return True
            return False
        
        def checkUppercase(password):
            for i in password:
                if i.isupper():
                    return True
            return False
        
        def checkDigit(password):
            for i in password:
                if i.isdigit():
                    return True
            return False
        
        def checkLength(password):
            if len(password) >= 6 and len(password) <= 20:
                return True
            return False
        
        def checkStrong(password):
            if checkLowercase(password) and checkUppercase(password) and checkDigit(password) and not checkConsecutive(password) and checkLength(password):
                return True
            return False
        
        def stepsRequiredMakeStrong(password):
            steps = 0
            if checkStrong(password):
                return 0
            if not checkLength(password):
                if len(password) < 6:
                    steps += 6 - len(password)
                else:
                    steps += len(password) - 20
                return steps
            if not checkLowercase(password):
                steps += 1
            if not checkUppercase(password):
                steps += 1
            if not checkDigit(password):
                steps += 1
            if checkConsecutive(password):
                steps += stepsRequiredMakeConsecutiveStrong(password)
            return steps
        
        return stepsRequiredMakeStrong(password)

s1 = Solution()
# print(s1.strongPasswordChecker("aaa111"))
# print(s1.strongPasswordChecker("aA1"))
print(s1.strongPasswordChecker("1111111111"))