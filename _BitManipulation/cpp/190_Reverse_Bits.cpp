#include <iostream>
// Time:  O(logn) = O(32)
// Space: O(1)
using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t result = 0;
        int count = 32;
        while (count--) {
            result <<= 1;
            result |= n & 1;
            n >>= 1;
        }
        return result;
    }

    uint32_t reverseBits2(uint32_t n) {
        uint32_t result = 0;
        uint32_t mask = 1;

        for(int i=0;i<32;i++){
            result <<= 1;
            result |= n&mask;
            n>>=1;
        }
        return result;
    }
};

int main(){
    int n = 43261596;
    Solution obj;
    cout << obj.reverseBits2(n);
    return 0;
}