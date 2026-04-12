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
        groupPrev = dummy

        while True:
            kth = self.get_kth(groupPrev, k)

            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        
        return dummy.next

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr

    def reverseKGroup_myanswer(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        現在のノードから次ノードがK-1個あるかによらず反転していく
        仮にK未満出会った場合にはそのグループのみ反転し直す実装を考えた
        →反転し直すという楽観的な実装だが、K未満の処理に対してコード少し余分

        Time Complexity: O(N)
        Space Complexity: O(1) because we jus opperate pointer
        """
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