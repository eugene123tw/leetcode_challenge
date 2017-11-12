#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

int main(){

    int a[5] = {1,3,5,7,9};
    int b[4] = {2,4,6,8};

    ListNode* l1(0);

    ListNode* ptr = l1;

    for(auto i:a){
        ListNode* newNode = new ListNode(i);
        ptr->next = newNode;
        ptr = ptr->next;
    }

    cout<< l1->next->val <<endl;

    return 0;
}