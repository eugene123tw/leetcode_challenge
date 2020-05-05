import operator
import numpy as np
from functools import reduce

class Solution(object):
    def singleNumber(self, nums):
        one, two = 0, 0
        for x in nums:
            two = two | (one & x)
            one = operator.xor(one,x)
            common_bit_mask = ~(one & two)
            one, two = common_bit_mask & one , common_bit_mask & two

        return one


if __name__ == '__main__':

    # nums = [-1]
    nums = [3,3,3,2]
    # nums = [2,4,2,2,4,4]
    # nums = [2, 4, 2, 2, 4, 4, 5]

    obj = Solution()
    num = obj.singleNumber(nums)
    print(num)
