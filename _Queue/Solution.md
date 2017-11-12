# Queue
## 239. Sliding Window Maximum
Given an array nums, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the `k` numbers in the window. Each time the sliding window moves right by one position.

For example,
Given `nums = [1,3,-1,-3,5,3,6,7]`, and `k = 3`.
```
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```
Therefore, return the max sliding window as `[3,3,5,5,6,7]`.

Note:  
You may assume `k` is always valid, ie: $1 \leq k \leq input$ array's size for non-empty array.

Follow up:  
Could you solve it in linear time?

### My solution: Ugly

```py
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
        result = []
        queue = {}
        
        if k==0:
            return result

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
```