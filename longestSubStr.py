class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        final = 0
        arr = []
        past = {}
        for i in range(len(s)):
            if s[i] in past:# duplicate 
                arr.append(final-start + 1)
                start = max(past[s[i]] + 1,start)
                final = i
                past[s[i]] = i
            else:# letter not in past
                past[s[i]] = i # sets the dict to correspond to position in string
                final = i
        arr.append(final-start + 1)

        if(len(s) == 0):
            return 0
        return max(arr)