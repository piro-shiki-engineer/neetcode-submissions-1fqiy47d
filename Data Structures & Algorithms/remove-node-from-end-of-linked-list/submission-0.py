# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Just count up the number of pointer changes until n.
    → 前からn番目のノードを削除する際にはよいが、実際には後ろからn番目の削除が要求されていた。
    
    解法：Two pointerを使って回答する。
    具体的にはleftポインタを設置し、rihgtをn個先のノードに設定する。
    leftを一つずつ動かして、最終的にrightのnextが自ノードがNoneであるならば、leftが削除対象となるノードである。
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right: # n先のノードに移動
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete the left'node
        left.next = left.next.next

        return dummy.next
