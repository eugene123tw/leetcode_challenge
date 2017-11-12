import collections

def find_max(num_list,begin=0):
    max = num_list[0]
    key = 0
    for i in range(len(num_list)):
        if num_list[i]>max:
            max = num_list[i]
            key = i+begin
    return max,key

class Solution:
    def maxSlidingWindow(self, nums, k):
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out

    def maxSlidingWindow1(self, nums, k):
        result = []
        queue = {}

        for i in range(len(nums)-k+1):

            if len(queue)==0:
                max, key = find_max(nums[i:i+k],begin=i)
                queue[key] = max
            else:
                if queue[key]>nums[i+k-1]:
                    max = queue[key]
                else:
                    queue = {}
                    max = nums[i+k-1]
                    key = i+k-1
                    queue[key] = max

            if i+1 > key:
                queue = {}

            result.append(max)

        return result

if __name__ == '__main__':
    nums,k = [1, 3, -1, -3, 5, 3, 6, 7], 3

    obj = Solution()
    print(obj.maxSlidingWindow(nums,k))
