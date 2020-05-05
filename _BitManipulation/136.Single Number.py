import operator
from functools import reduce

class Solution:
    def singleNumber(self, nums):
        return reduce(operator.xor, nums)


if __name__ == '__main__':
    nums = [17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6]
    # nums = [2,2,1]
    obj = Solution()
    num = obj.singleNumber(nums)

    print(num)