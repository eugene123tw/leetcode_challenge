class Solution(object):
    def missingNumber(self, nums):
        res = 0
        for i in range(len(nums)):
            res = res^(i^nums[i])

        print("Res:%d, i:%d"%(res,i))

        return res^(i+1)


if __name__ == '__main__':
    nums = [0,1,2,3,4]
    obj = Solution()
    print(obj.missingNumber(nums))