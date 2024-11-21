# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
    # def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # nodeslist=[]
        # curr=head
        # while curr:
        #     nodeslist.append(curr)
        #     curr=curr.next
        # # nodeslist.append(ListNode())
        # if n == len(nodeslist):
        #     return head.next
        # nodeslist[-n-1].next=nodeslist[-n].next
        # return head

        dummy = ListNode(0, head)
        fast=head
        slow=dummy

        for i in range(n):
            fast=fast.next
        while fast:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return dummy.next


        