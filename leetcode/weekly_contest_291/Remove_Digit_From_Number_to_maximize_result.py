class Solution(object):
    def removeDigit(self, number, digit):
        """
        :type number: str
        :type digit: str
        :rtype: str
        """
        if not number or not digit:
            return number
        digit = str(digit)
        number = str(number)
        if digit not in number:
            return number
        else:
            return self.removeDigit(number.replace(digit, "", 1), digit)