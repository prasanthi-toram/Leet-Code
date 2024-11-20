# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # def add(self,l1,l2,r):

    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=new= ListNode()
        rem=0

        while l1 or l2:
            v1=l1.val if l1 else 0
            v2=l2.val if l2 else 0


            new.next=ListNode((v1+v2+rem)%10)
            rem=(v1+v2+rem)//10
            new=new.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if rem>0:
            new.next=ListNode(rem)
        return dummy.next


        