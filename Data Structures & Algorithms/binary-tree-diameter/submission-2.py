# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """birnay tree's diameter is 2ノード間の最長の長さ
    - diameter have also mean にノード間のエッジの数
    - Do not include the same node
    - We dont need have to take care of which right or left's node.
    - Just need level → BFS

    [node, diameter] 
    Why first node's diameter is 0 ?
    because we can count up if next right or left node exist

    方針：任意のノードからみた時の左の木の高さと右の木の高さをそれぞれ求める

    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr: Optional[TreeNode]) -> int:
            if not curr:
                return 0
            
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)

            return 1 + max(left, right) # left, rightから見たときのcurrまでの高さを＋1している
        
        dfs(root) # 実行するのを忘れないこと
        
        return self.res