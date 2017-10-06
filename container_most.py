import numpy as np

# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         max_area = 0
#
#         for i in range(0,len(height)):
#             for j in range(i+1,len(height)):
#                 max_area = max(max_area,min(height[i],height[j])*(j-i))
#
#         return max_area

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        i = 0
        j = len(height)-1

        while(i!=j):
            max_area = max(max_area, min(height[i], height[j]) * (j - i))
            if np.argmin([height[i], height[j]])==0:
                i+=1
            else :
                j-=1
        return max_area



if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # height = [1, 1]
    # height = [2, 1]
    obj = Solution()
    print(obj.maxArea(height))