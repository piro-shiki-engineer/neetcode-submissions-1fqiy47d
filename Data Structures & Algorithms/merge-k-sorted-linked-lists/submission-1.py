# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    given k linked list.
    objective: merge all linked list to one linked list.

    diffterenc length of linked list
    simple solution: just compare node one by one and rejoined the node each cases like

    i dont understand key which is to solve efficietnly. so, lets think the example1.

    example1.
    [[1,2,4],[1,3,5],[3,6]]
    l1 = [1, 3, 5], l2 = [1, 2, 4], l3 = [3, 6]
    just think the simple soltion and think as arrays because it's easy to express linked list.
    l1[0] <= l2[0], l1[1] > l2[0] →  l1 = [1, 1, 3, 5] l2 = [2, 4]
    l1[0],l1[1] <= l2[1](alerady know), l1[2] > l2[1]→  l1 = [1, 1, 2, 3, 5] l2 = [4]
    l1[0], l1[1], l1[2] <= l2[2](alerady know) l1[3] <= l2[2] l1[4] > l2[2] →  l1 = [1, 1, 2, 3, 5] l2 = []
    
    l1 = [1, 1, 2, 3, 5] l3 = [3, 6]
    l1[0],l1[1],l1[2], l1[3] <= l2[1], l1[4] > l3[0]→  l1 = [1, 1, 2, 3, 5] l2 = [4]
    l1[0], l1[1], l1[2], l1[3] <= l2[2](alerady know) l1[4] <= l2[2] l1[4] > l2[2] →  l1 = [1, 1, 2, 3, 5] l2 = []

    record the point previous node is inserted and reuse for comparing.
    it's ok if the numbers of linked list is just TWO.
    I cant use binary search because target is sorted list.
    Maybe I think we can use binary search for just LinkedList's head.
    how reuse it's the case

    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        # 最初のリストから開始（Noneでも問題なし）
        result = lists[0]
        
        # 残りのリストを順次マージ
        for i in range(1, len(lists)):
            head = lists[i]
            if not head:
                continue
                
            # resultリストに挿入していく
            dummy = ListNode()
            dummy.next = result
            prev = dummy
            cur = result
            
            while head and cur:
                if head.val <= cur.val:
                    next_head = head.next
                    prev.next = head
                    head.next = cur
                    prev = head
                    head = next_head
                else:
                    prev = cur
                    cur = cur.next
            
            if head:
                prev.next = head
                
            result = dummy.next
        
        return result