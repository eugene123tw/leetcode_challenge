class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        buffer_dict = {}

        for i in range(0, len(nums)):
            if nums[i] in buffer_dict:
                return [buffer_dict[nums[i]], i]
            else:
                buffer_dict[target - nums[i]] = i


if __name__ == '__main__':
    obj1 = Solution()

    print(obj1.twoSum(nums=[2, 7, 11, 15],target=9))