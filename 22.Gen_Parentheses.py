class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        for i in range(1,n+1):
            print("("*i)



if __name__ == '__main__':
    n = 2

    obj = Solution()
    obj.generateParenthesis(n)