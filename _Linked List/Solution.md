# LinkedList - Solution
## 23. Merge k Sorted Lists
Merge `k` sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
```
ls1 = [1,2,4]
ls2 = [3,4,5]
ls3 = [2,3,6]
```
### My method: Merge lists one by one
Algorithm:  
Convert merge $k$ lists problem to merge 2 lists $(k-1)$ times.
Ex: Merge one ls1, ls2 first, then merge ls3.

```cpp
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
```

### Approach #2 Compare one by one and optimized using Priority queue [Accepted]


## 92. Reverse Linked List II
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:  
Given `1->2->3->4->5->NULL`, `m = 2` and `n = 4`,  

return `1->4->3->2->5->NULL`.  

Note:  
Given m, n satisfy the following condition:  
$1 \leq m \leq n \leq length$ of list.  

