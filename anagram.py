class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        arr = []
        check = {}
        for word in strs:
            tempCount = 1
            for letter in word:
                tempCount *= (ord(letter))
            if tempCount in check:#checks if anagram is unique
                check[tempCount].append(word)# adds the anagram word to a list
            else: #anagram is not unique
                check[tempCount] = [word]
        for key, value in check.items():
            arr.append(value)
        return arr
    #100/101 test case passed