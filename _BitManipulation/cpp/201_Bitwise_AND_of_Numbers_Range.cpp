#include <iostream>
#include <cmath>
using namespace std;
class Solution {
public:
    int rangeBitwiseAnd(int m, int n) {
        double fac = 0;
        
        while(m!=n){
            m >>= 1;
            n >>= 1;
            fac+=1;
        }

        return (m&n)*pow(2,fac);
    }
};

int main(){
    int m = 0;
    int n = 2147483647;
    
    Solution obj;
    cout << obj.rangeBitwiseAnd(m,n);
    return 0;
}