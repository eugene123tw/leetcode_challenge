# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if n==0:
            return head

        cnt = 0

        ptr = head
        while ptr!=None:
            cnt+=1
            ptr=ptr.next

        n = cnt-n+1

        ptr = head

        cnt = 0

        while ptr!=None:

            if n==1:
                head = ptr.next
                break

            cnt+=1

            if (cnt+1)==n:
                ptr.next = ptr.next.next
                break
            else:
                ptr=ptr.next

        return head



if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    obj = Solution()
    head = obj.removeNthFromEnd(head,0)

    pass