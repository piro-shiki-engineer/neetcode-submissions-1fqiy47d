# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    What's "good" node ? So, Let's clarify more.
    The path from root to node x have have  no nodes which is greater than x.

    I think we should use DFS because the 

    """
    def goodNodes_myanswer(self, root: TreeNode) -> int:
        """
        BFS approach
        """
        if not root:
            return 0
        
        res = 0
        queue = collections.deque()
        queue.append((root, -float('inf'))) # [Node, maxValue_current]

        while queue:
            node, currMax = queue.popleft()
            if node.val >= currMax:
                res += 1
        
            if node.left:
                queue.append((node.left, max(currMax, node.val)))
            
            if node.right:
                queue.append((node.right, max(currMax, node.val)))

        return res

    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS approach
        """
        def dfs(node, maxVal):
            if not node:
                return 0
            
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res
        
        return dfs(root, root.val)