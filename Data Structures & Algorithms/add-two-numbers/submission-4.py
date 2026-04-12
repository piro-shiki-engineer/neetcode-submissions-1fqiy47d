# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    element: non-negative integer → 0,1,2,3,4 ...
    
    - carry up case like this example. 17 + 23 = 40
    - different numbers of digits like this example. 123 + 23 = 146
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        cur1 = l1
        cur2 = l2
        dummy = cur = ListNode()
        carry_up = False

        while cur1 or cur2 or carry_up:
            total = 1 if carry_up else 0
            total += (cur1.val if cur1 else 0)
            total += (cur2.val if cur2 else 0)

            carry_up = False

            if total >= 10:
                total = total % 10
                carry_up = True
            
            cur.next = ListNode(total)
            cur = cur.next
            if cur1:
                cur1 = cur1.next if cur1.next  else None
            
            if cur2:
                cur2 = cur2.next if cur2.next else None

        return dummy.next