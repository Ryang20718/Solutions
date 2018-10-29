from collections import deque
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stac = []
        dicti = {'(':')', '[':']', '{':'}'}
        if(len(s) == 0):
            return True
        for i in s:
            if(i in dicti):
                stac.append(i) # check if each char is a left paren, bracket, or curly
            else:
                if(dicti[stac.pop()] != i):
                    return False#pop all corresponding paren
        return stac == [0]

        