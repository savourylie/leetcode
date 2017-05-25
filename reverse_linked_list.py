# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        pprev = prev = None
        current = head

        while current is not None:
            if prev is None:
                prev = current
            else:
                prev.next = pprev
                pprev = prev
                prev = current
            current = current.next

        prev.next = pprev

        return prev