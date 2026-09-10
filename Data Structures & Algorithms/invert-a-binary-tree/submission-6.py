# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Task: Return inverted tree

    Normal: a node have left and right node.
    node.left, node.right = node.right, node.left

    Edge 1: a node is None
    just do nothing. we need handle it

    Walk through tree by using dfs. I treverse right node first, and then left node.

    Time: O(n)
    Space: O(n) recursion stack
    n is the total of nodes.
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
        