#include <iostream>
#include <vector>
#include <queue>
#include <iterator>

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
        if(lists.empty()){
            return nullptr;
        }
        while(lists.size()>1){
            lists.push_back(mergeTwoLists(lists[0],lists[1]));
            lists.erase(lists.begin());
            lists.erase(lists.begin());
        }
        return lists.front();
    }

    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if(l1 == nullptr){
            return l2;
        }
        if(l2 == nullptr){
            return l1;
        }
        if(l1->val <= l2->val){
            l1->next = mergeTwoLists(l1->next, l2);
            return l1;
        }
        else{
            l2->next = mergeTwoLists(l1, l2->next);
            return l2;
        }
    }
};

int main(){
    vector<int> a = {45, 47, 49, 80, 97};
    vector<int> b = {20, 24, 31, 65, 87};
    vector<int> c = {33, 45, 56, 64, 93};
    vector<int> d = { 3, 19, 35, 38, 59};

    ListNode* l1 = vector2ListNode(&a);
    ListNode* l2 = vector2ListNode(&b);
    ListNode* l3 = vector2ListNode(&c);
    ListNode* l4 = vector2ListNode(&d);

    vector<ListNode*> lists;
    lists.push_back(l1);
    lists.push_back(l2);
    lists.push_back(l3);
    lists.push_back(l4);

    Solution obj;
    ListNode* result = obj.mergeKLists(lists);
    ListNode* ptr = result;

    while(ptr){
        cout<<ptr->val<<endl;
        ptr = ptr->next;
    }

    return 0;
}