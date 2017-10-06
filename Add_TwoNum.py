# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# my solution
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         ptr1 = l1
#         ptr2 = l2
#         val = 0
#         carry = 0
#         head=ListNode(-1)
#         ptr = head
#
#
#         while ptr1!=None and ptr2!=None :
#
#             ptr.next = ListNode((ptr1.val+ptr2.val+carry)%10)
#
#             if (ptr1.val+ptr2.val+carry)//10 !=0:
#                 carry = 1
#             else:
#                 carry = 0
#
#             ptr = ptr.next
#             ptr1 = ptr1.next
#             ptr2 = ptr2.next
#
#         while ptr1!=None:
#             ptr.next = ListNode((ptr1.val + carry) % 10)
#             if (ptr1.val+carry)//10 !=0:
#                 carry = 1
#             else:
#                 carry = 0
#
#             ptr = ptr.next
#             ptr1 = ptr1.next
#
#         while ptr2!=None:
#             ptr.next = ListNode((ptr2.val + carry) % 10)
#             if (ptr2.val+carry)//10 !=0:
#                 carry = 1
#             else:
#                 carry = 0
#
#             ptr = ptr.next
#             ptr2 = ptr2.next
#
#         if carry!=0:
#             ptr.next = ListNode(1)
#
#
#         return head.next

# official solution
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ptr1 = l1
        ptr2 = l2
        carry = 0
        head=ListNode(0)
        ptr = head

        while ptr1!=None or ptr2!=None :

            x = ptr1.val if (ptr1!=None) else 0
            y = ptr2.val if (ptr2!=None) else 0
            sum = (x+y+carry)
            carry = sum // 10
            ptr.next = ListNode( sum % 10)
            ptr = ptr.next
            if ptr1 != None: ptr1 = ptr1.next
            if ptr2 != None: ptr2 = ptr2.next


        if carry>0:
            ptr.next = ListNode(carry)

        return head.next


if __name__ == "__main__":
    l1 = ListNode(5)
    # l1.next = ListNode(5)
    # l1.next.next = ListNode(7)
    # l1.next.next.next = ListNode(2)

    l2 = ListNode(7)
    # l2.next = ListNode(5)
    # l2.next.next = ListNode(4)
    # l2.next.next.next = ListNode(2)

    obj1 = Solution()
    obj1.addTwoNumbers(l1,l2)