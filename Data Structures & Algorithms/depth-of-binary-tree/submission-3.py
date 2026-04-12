# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    baseケースつまり参照しているノードが場合は加算しない

    それぞれのSubTreeでDFSをおこなって、最終的により深い部分木の結果を足していく
    Recursive DFS Depth First Search 
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
