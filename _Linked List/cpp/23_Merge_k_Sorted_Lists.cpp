#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
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

class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        
    }
};

int main(){
    vector<int> a = {1,3,5,7,9};
    vector<int> b = {2,4,6,8};
    vector<int> c = {877,433,22,124};

    ListNode* l1 = vector2ListNode(&a);
    ListNode* l2 = vector2ListNode(&b);
    ListNode* l3 = vector2ListNode(&c);

    vector<ListNode*> lists;
    lists.push_back(l1);
    lists.push_back(l2);
    lists.push_back(l3);

    return 0;
}