#include <iostream>
#include <vector>

using namespace std;

int str2binary(string str){
    int result = 0;
    for(auto c:str){
        result |= 1 << (((int)c) - 97 + 26);
    }
    return result;
}

class Solution {
public:
    int maxProduct(vector<string>& words) {
        
        vector<int> value;
        int max_len = 0;
        int product = 0;

        for(int i=0;i<words.size();i++){
            value.push_back(str2binary(words[i])); 
        }


        for(int i=0;i<words.size();i++){
            for(int j=i+1;j<words.size();j++){
                if((value[i] & value[j])==0){
                    product = words[i].length() * words[j].length();
                    if(product > max_len){
                        max_len = product;
                    }
                }
            }
        }

        return max_len;
    }
};

int main(){
    vector<string> words = {"a", "aa", "aaa", "aaaa"};
    
    Solution obj;
    cout << obj.maxProduct(words) << endl ;

    return 0;
}