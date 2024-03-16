# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev=ListNode(0)
        temp=prev
        while head:
            if head.val !=val:
                prev.next=head
                prev=prev.next
            head=head.next
        prev.next=None
        return temp.next