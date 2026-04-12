# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    深さ優先探索で実装したほうが左部分木と右部分木に分けて考えられる
    SubrootもDFSでいいかも

    I want to use DFS Because we can inplement by using BFS or DFS
    Basically DFS is eaiser than BFS by using Recusice DFS.

    we need the function which can find out two binary tree is equals
    Also, I inplement this function by using DFS.
    lets call this funciton isSameTree
    """  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            
            if self.isSameTree(node, subRoot):
                return True
            
            if node.left:
                queue.append(node.left) 
            if node.right:
                queue.append(node.right)

        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)