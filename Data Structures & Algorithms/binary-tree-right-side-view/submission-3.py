# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    My Idea is simple
    Base sollution is DFS but if we append just append right from current node

    In other words, this problem means most right node's value each level.
    I think we should use Breath First search because we want most right node's value each level.
    Time Comlexity: O(logN) or O(H) h is height of BT
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        if not root:
            return res

        queue = collections.deque([root])
        while queue:
            num_of_curr_level = len(queue)
            values_curr_level = []
            for i in range(num_of_curr_level):
                node = queue.popleft()
                if node:
                    values_curr_level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if values_curr_level:
                res.append(values_curr_level[-1])

        return res          
