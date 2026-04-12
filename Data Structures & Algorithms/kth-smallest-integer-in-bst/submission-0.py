# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    We can break down the problem to more small pieces problems by using recursive

    at the root node's problem fucntion check kth smallest values
    next, if the left subtree exsit the problem is to get k-1 th smallest value
    Until there is no left subtree, you can solve k-(the number of left subtree have nodes)-1 th samllest value

    root.left.val < root.val < root.right.val
    """
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        BruteForce
        get every nodes in tree into array
        after that, sort the array and get k th value

        Time: O(nlong)
        Space: O(n)
        """
        nums = []

        def dfs(node):
            nonlocal nums
            if not node:
                return
            
            nums.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        nums.sort()

        return nums[k-1]
