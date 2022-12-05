"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l1 = list()
        ptr = head
        while ptr != None:
            l1.append(ptr)
            ptr = ptr.next
        length = (len(l1) / 2)
        ptr = head
        while length > 0:
            ptr = ptr.next
            length -= 1
        return ptr