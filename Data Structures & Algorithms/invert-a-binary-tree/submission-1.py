# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    invert 反転

    すぐに回答できなかった理由TreeNodeの定義をしっかり確認できていなかった。
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        DFS (Depth First Search)により探索している。
        """  
        if not root:
            return None
        
        # tmpに保存してもいいが、Pythonは同時に値を操作できるため一度の操作で行える
        # root.left→root.right root.right→root.leftになることはわかっている。
        # またそれぞれSubTreeの反転することはわかっている
        root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        
        return root