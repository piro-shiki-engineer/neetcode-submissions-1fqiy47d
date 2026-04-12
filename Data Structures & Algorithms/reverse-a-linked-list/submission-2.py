# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         """
#         Args:
#             val(int): ノードが持つ値
#             next(ListNode):次ノードのアドレス
#         """

#         self.val = val
#         self.next = next

class Solution:
    """
    ListNodeがコメントアウトされているが、ここでコメントアウトを外して再定義する必要はない
    ポインタの付け替えを一つずつ行えば最終的にリバースされる
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            temp = current.next # 次ノードへのポインタを一時保存
            current.next = prev # 次ノードを前のノードへのポインタへ置き換え
            prev = current
            current = temp
        
        return prev



