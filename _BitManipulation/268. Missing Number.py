class Solution(object):
    def missingNumber(self, nums):
        res = 0
        for i in range(len(nums)):
            res = res^(i^nums[i])

        return res^(i+1)

    def missingNumber1(self, nums):
        res = []

        for i in range(len(nums)+1):
            res.append(i)

        for i in range(len(nums)):
            if res[i]^nums[i]!=0:
                return res[i]


if __name__ == '__main__':
    nums = [0,1,3,4]
    obj = Solution()
    print(obj.missingNumber1(nums))