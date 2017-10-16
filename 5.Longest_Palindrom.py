import numpy as np

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        dp = np.full((len(s),len(s)), False, dtype=bool)
        longeset = ""

        for i in range(len(s),-1,-1):
            for j in range(i,len(s)):
                if s[i]==s[j] and (j-i<2 or dp[i+1,j-1]):
                    dp[i,j]=True
                    if len(s[i:(j+1)])> len(longeset):
                        longeset = s[i:(j+1)]

        return longeset

if __name__ == '__main__':


    obj = Solution()
    # "ranynar"
    longeset = obj.longestPalindrome("abaabc")
    print(longeset)