from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        # Merge list one by one

        if len(lists)==0 or len(lists)==1:
            return lists

        result = lists[0]

        for i in range(1,len(lists)):
            result = self.mergeTwoLists(result, lists[i])

        return result

    def mergeTwoLists(self, l1, l2):

        merge = ListNode(-1)
        ptr_merge = merge
        ptr1,ptr2 = l1,l2

        while ptr1 != None or ptr2 != None:

            x = ptr1.val if (ptr1 != None) else 9999999
            y = ptr2.val if (ptr2 != None) else 9999999

            ptr_merge.next = ListNode(min(x,y))
            ptr_merge = ptr_merge.next
            if x>y:
                ptr2 = ptr2.next
            else:
                ptr1 = ptr1.next

        return merge.next

    def mergeKLists1(self, lists):
        # Priority Queue

        head = point = ListNode(0)
        q = PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))
        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            point = point.next
            node = node.next
            if node:
                q.put((node.val, node))
        return head.next


if __name__ == "__main__":
    ls1 = [45, 47, 49, 80, 97]
    ls2 = [20, 24, 31, 65, 87]
    ls3 = [33, 45, 56, 64, 93]
    ls4 = [ 3, 19, 35, 38, 59]


    full_vector = [ls1,ls2,ls3,ls4]
    node_vector = []

    for vector in full_vector:
        linkedList = ListNode(0)
        ptr = linkedList

        for num in vector:
            ptr.next = ListNode(num)
            ptr = ptr.next

        node_vector.append(linkedList.next)

    obj = Solution()
    result = obj.mergeKLists1(lists=node_vector)

    ptr = result

    while ptr:
        print(ptr.val)
        ptr = ptr.next


    pass