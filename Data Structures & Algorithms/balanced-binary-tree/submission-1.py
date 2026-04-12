# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    height-balanced tree: 左部分木と右部分木の高さの差が1以下
    それぞれの高さを求めて比較しその時点で
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        def dfs(node: Optional[TreeNode]) -> tuple[bool, int]:
            if not node:
                return True, 0
            
            leftBlanced, leftHeight = dfs(node.left)
            rightBlanced, rightHeight = dfs(node.right)

            if not (leftBlanced and rightBlanced) or not abs(leftHeight-rightHeight) <= 1:
                return False, 0

            # if not abs(leftHeight-rightHeight) <= 1:
            #     return False, 0

            return True, 1 + max(leftHeight, rightHeight) 
        
        return dfs(root)[0]