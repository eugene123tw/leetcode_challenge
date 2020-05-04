class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1)%2 == 0:

            return (nums1[len(nums1)//2]+nums2[len(nums2)//2])//2


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]

    obj = Solution()
    print(obj.findMedianSortedArrays(nums1,nums2))