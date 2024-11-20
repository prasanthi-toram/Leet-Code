# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodeslist=[]
        curr=head
        while curr:
            nodeslist.append(curr)
            curr=curr.next
        # nodeslist.append(ListNode())
        if n == len(nodeslist):
            return head.next
        nodeslist[-n-1].next=nodeslist[-n].next
        return head


        