# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
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


if __name__ == '__main__':
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)
    l1.next.next.next = ListNode(7)
    l1.next.next.next.next = ListNode(9)

    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    obj = Solution()
    obj.mergeTwoLists(l1,l2)