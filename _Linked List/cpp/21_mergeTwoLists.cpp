#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode(0);
        ListNode* ptr = result;

        while(l1!=NULL || l2!=NULL){
            int x =  l1!=NULL?l1->val:9999999;
            int y =  l2!=NULL?l2->val:9999999;

            ptr->next = new ListNode(x>y?y:x);
            ptr = ptr->next;

            if(x>y){
                l2 = l2->next;
            }else{
                l1 = l1->next;
            }            
        }
        return result->next;
    }
};

ListNode* vector2ListNode(vector<int> *ar_ptr){
    ListNode* list = new ListNode(0);
    ListNode* ptr = list;
    for(vector<int>::iterator i=ar_ptr->begin();i<ar_ptr->end();i++){
        ListNode* newNode = new ListNode(*i);
        ptr->next = newNode;
        ptr = ptr->next;
    }
    return list->next;
}

void printList(ListNode* inList){
    
    ListNode* ptr = inList;
    while(ptr!=NULL){
        cout<< ptr->val << endl;
        ptr = ptr->next;
    }
}

int main(){

    vector<int> a = {1,3,5,7,9};
    vector<int> b = {2,4,6,8};

    ListNode* l1 = vector2ListNode(&a);
    ListNode* l2 = vector2ListNode(&b);
    ListNode* result;

    Solution obj;
    result = obj.mergeTwoLists(l1,l2);

    printList(result);

    return 0;
}