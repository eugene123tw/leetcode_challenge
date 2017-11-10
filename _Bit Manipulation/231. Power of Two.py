class Solution(object):
    def isPowerOfTwo(self, n):
        # if  n = 4 = 0100
        # n - 1 = 3 = 0011
        # n&n-1 = 0000 -> Power of two

        return n > 0 and not(n&n-1)

if __name__ == '__main__':
    n = 4
    obj = Solution()
    print(obj.isPowerOfTwo(n))