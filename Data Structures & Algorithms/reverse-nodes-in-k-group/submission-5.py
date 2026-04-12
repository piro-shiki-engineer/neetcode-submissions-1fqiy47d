# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    how to separate the LinkedList per k. → I think it's not need extra spcae more than O(1)
    I think just count up moving next node until k.
    After that, reverse Linked List each other.
    Finally, just join all Linked List.
    k個も要素があるLinked
    How to check the numer of nodes excluding current.
    I think we can use slow & fast pointer.
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = head
        count_node = 0
        prevGroupEnd = dummy
        prev = None
        
        while current:
            if count_node == 0:  # 新しいグループ開始時
                originalGroupStart = current  # 反転前の状態を保存
                
            count_node += 1
            
            if count_node <= k:  # k個以下のグループ内
                # 反転処理（共通）
                temp = current.next 
                current.next = prev
                prev = current
                current = temp # 次ノードに移動
                
                if count_node == k:  # グループ完成時のみ
                    # 接続処理
                    prevGroupEnd.next = prev  # 前のグループを現在のグループの新しい先頭に接続
                    prevGroupEnd = originalGroupStart  # 元のグループの最初（反転後は最後）を次のprevGroupEndに
                    count_node = 0           # カウントリセット
                    prev = None              # 次のグループ用にリセット
            
            else:  # k個未満の残りノード - 反転した部分を元に戻す
                # 反転した部分を元に戻す
                curr = prev
                new_prev = None
                for i in range(count_node - 1):
                    temp = curr.next
                    curr.next = new_prev
                    new_prev = curr
                    curr = temp
                # 元に戻した状態で接続
                prevGroupEnd.next = new_prev
                break
        
        # k個未満で終了した場合の残りノード処理
        if count_node > 0 and count_node < k:
            # 反転した部分を元に戻す
            curr = prev
            new_prev = None
            for i in range(count_node):
                temp = curr.next
                curr.next = new_prev
                new_prev = curr
                curr = temp
            # 元に戻した状態で接続
            prevGroupEnd.next = new_prev
        
        return dummy.next