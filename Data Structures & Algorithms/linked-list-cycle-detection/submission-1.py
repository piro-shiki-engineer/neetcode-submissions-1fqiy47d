# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    simple: solution is just easy. This is how count up value numvber of occurrences by using Hashset
    I wonder if there is a edge case like refer to own themself

    You should add not value but Object that means LinkNode's Object
    Linked Listの特性により必ずしも次のノードのみでなく次の次のノードもO(1)でアクセスできる特性をもつ
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        フロイドの循環検出法
        一つずつ進むポインターと二つずつ進むポインターがある場合
        ギャップが必ず一つずつ縮まっていく、そのためどこで再開できその場合はサイクルが存在する
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False

    def simple_hasCycle(self, head: Optional[ListNode]) -> bool:
        cur = head
        hashSet = set()

        while cur:
            if cur in hashSet:
                return True
            hashSet.add(cur)
            cur = cur.next
        
        return False