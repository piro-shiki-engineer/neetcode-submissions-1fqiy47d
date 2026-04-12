# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    return the maximum value
    the value is  in a binary tree is a sequence of nodes where each pair of adjacent nodes has an edge connecting them. 
    It's ok to uncontain root node.
    
    We can break down smaller problems.
    I want problem more clarify, so lets think about example2 .

    Ex2)
    Input: root = [-15,10,20,null,null,15,5,-5]
    Output: 40

    how do you get the maximu value I wanna think most depth 

    Neetcode:
    ノードでの分岐は一度しかできない→ぱすにならない
    分岐を含むをパスの場合、親に最大パスとして渡せない

    分岐をゆるす場合： ノード自身の値＋左部分木最大＋右部分木最大
    分岐を許さない場合：Max(ノード自身の値＋左部分木最大, ノード自身の値＋右部分木最大)
    →親ノードに渡す最大は分岐を許さない場合の値
    →全体としての最大は分岐を許す場合で更新する

    """
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(node: Optional[TreeNode]) -> int:
            # retrun max path without split
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)

            # それぞれの最大が負の場合には加算しない
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # update global max path WITH split
            res[0] = max(res[0], node.val + leftMax + rightMax)

            # return maxpath without split
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        
        return res[0]