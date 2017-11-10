import operator
from functools import reduce

class Solution:
    def rangeBitwiseAnd(self, m, n):
        fac = 0

        while(m!=n):
            m >>= 1
            n >>= 1
            fac+=1

        return (m&n)*2**fac

if __name__ == "__main__":

    m, n = 108, 110
    obj = Solution()
    print(obj.rangeBitwiseAnd(m,n))