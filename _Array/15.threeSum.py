class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()

        for i in range(0,len(nums)-2):
            l = i+1
            r = len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])

                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1

                    l+=1
                    r-=1

        return res


if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    nums = [0,0,0,0]
    obj = Solution()
    print(obj.threeSum(nums))