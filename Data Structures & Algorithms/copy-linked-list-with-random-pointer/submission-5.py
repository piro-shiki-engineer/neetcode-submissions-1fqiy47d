"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    """
    自分の考え
    パス1：LinkedListの部分をコピーする
    パス2：randomの部分を補填する
        パターン1：Nullに繋がる
        パターン2：現ノードよりも前のノードに繋がる
        パターン2：現ノードよりも後ののノードに繋がる→これの繋げ方がわからない

    解説
    パス1：ノードだけをコピーして、コピー元とコピー先の関係を辞書で管理
    パス2：next、randomを辞書で読み替えて値を挿入する→接続関係を繋げる
    """

    def unrecommend_copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        import copy
        return copy.deepcopy(head)
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            
            cur = cur.next
        
        return oldToCopy[head]

       