# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    I want to use DFS because it's more easy to implentment than DFS.

    BST is consisted of small pices of BST.
    
    Som we can break down to small check process and more easily.

    and we can check call function recuersivly and
    The left subtree of every node contains is less than the current node's key
    The right subtree of every node contains is greather than the current node's key

    Base case if currenet is None, return True
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node: Optional[TreeNode], minmum, maximum) -> bool:
            if not node:
                return True

            if node.val <= minmum:
                return False
            
            if node.val >= maximum:
                return False

            minmum = min(minmum, node.val)
            maximum = max(maximum, node.val)

            return validate(node.left, minmum, node.val) and validate(node.right, node.val, maximum)

        return validate(root, -float('inf'), float('inf'))