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
    def kthSmallest_Brute(self, root: Optional[TreeNode], k: int) -> int:
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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        再帰的な動きを再帰呼び出しを行わずするには、call stack →　STACK　interatively

        再帰禁止時にStackを使用する時の説明：
        "I'm using a stack because stack's LIFO behavior perfectly replicates 
        recursive call patterns - the last function called returns first, 
        just like stack.pop() retrieves the most recently pushed item."

        左部分気を探索する前に現在のノードにポップバックするためにstackにアペンドする
        つまり左部分木を訪れる前にstackにappendし、それぞれ訪れた後にpopし現在何番目までわかっているかを更新する
        ポップバックした後にポップバックしたノードの右部分木を訪れる同じ操作を繰り返す
        """
        visited = 0
        stack = []
        cur = root

        while cur or stack: # 右ノードが存在しないケースがあるから orを使っている
            while cur:
                stack.append(cur)
                cur = cur.left

            cur = stack.pop() # 左のノードから一つ親のノードに戻る
            visited += 1
            if visited == k:
                return cur.val
            
            cur = cur.right
