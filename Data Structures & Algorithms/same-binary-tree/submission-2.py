from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    We just check the p and q'nodes eqauls each value and left subtree and right sub tree.
    I want to use the Breatch First Search. → Because we dont need come back parent node.
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue_p = deque([p])
        queue_q = deque([q])

        while queue_p and queue_q:
            node_p = queue_p.popleft()
            node_q = queue_q.popleft()

            if node_p:
                if not node_q:
                    return False
                
                queue_p.append(node_p.left)
                queue_p.append(node_p.right)
            
            if node_q:
                if not node_p:
                    return False
                queue_q.append(node_q.left)
                queue_q.append(node_q.right)
            
            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False
            
        return True