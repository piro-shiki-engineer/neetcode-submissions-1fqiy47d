# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    それぞれの現時点のノードを値を比較してより大きい
    Comapare value of nums1's current node and value of nums2's current node
    if　it is smaller than or equals the other nums's current value,
    swap the next pointer to the bigger node

    lets think examle1.

    Input: list1 = [1,2,4], list2 = [1,3,5]
    Output: [1,1,2,3,4,5]

    current1 = 1 ,current_2 = 1 in this case current1 <= current2

    so, update current1's next to current2's. and release current1 from list1.
    repeat this operation unitl either nums1 or nums2 is None

    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode() # 最終的な結果をnextに、一時的な値の保存にvalを利用する

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next # release the merge Node
            else:
                node.next = list2
                list2 = list2.next
            
            node = node.next
        
        node.next = list1 or list2 # 最終的にマージした結果がある方を格納する
        
        return dummy.next
                