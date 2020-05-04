#include <iostream>
#include <vector>
#include <deque>
using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> result;
        deque<int> d_queue;
        for(int i = 0; i!=nums.size();i++){
            while(!(d_queue.empty()) && nums[d_queue.back()]<nums[i]){
                d_queue.pop_back();
            }
            d_queue.push_back(i);
            
            if (d_queue.front() == i - k){
                d_queue.pop_front();
            }
            
            if(i >= (k - 1)){
                result.push_back(nums[d_queue.front()]);
            }
        }
        return result;
    }
};

int main(){
    vector<int> nums = {1,-1};
    int k = 1;
    Solution obj;
    vector<int> result = obj.maxSlidingWindow(nums,k);

    for(int i = 0; i!=result.size();i++){
        cout<< result[i] << endl;
    }

    return 0;
}