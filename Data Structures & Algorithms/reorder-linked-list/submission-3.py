# Definition for singly-linked list. 単方向リスト
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    We need to know the tail node.
    tail node doesnt have the vales means next pointer.→一つのポインターで実装しようとして効率的な方法がわからなかった
    思いついた回答：
    リバースしたheadを用意して、二つのLinked Listを組み直しながら指定のオーダでソートする
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # middle より　右の配列を逆順にソート
        second = slow.next # 2番目の配列の先頭は真ん中のノードから一つ右のノード
        prev = slow.next =  None # 2番目の配列と1番目の配列に分割 prevは現在参照している2番目の配列のノードの前のノード
        while second: 
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # 最後に結合
        first = head
        second = prev
        while second: #必ずfirst のノードがsecondより多いためsecondに依存する
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
