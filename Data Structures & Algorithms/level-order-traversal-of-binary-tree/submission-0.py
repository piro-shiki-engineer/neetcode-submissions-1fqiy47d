# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    We aim to return the array which contains array which have nodes at the same level
    I want to think about how to get same level nodes → I think we should use Breath first search
    because the algorithm gurentee that we can access the same level nodes

    and we should concern about using binary search tree
    so we can predict the number of nodes in next level and seperate if we reached the number

    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res

        queue = deque([root])
        curr_level_values = []
        curr_num_node = 1 # root number is definityly
        next_num_node = 0
        
        while queue:
            node = queue.popleft()
            if curr_num_node > len(curr_level_values):
                curr_level_values.append(node.val)
                
            else:
                res.append(curr_level_values)
                curr_level_values = [node.val]
                curr_num_node = next_num_node
                next_num_node = 0

            if node.left:
                queue.append(node.left)
                next_num_node += 1
            
            if node.right:
                queue.append(node.right)
                next_num_node += 1

        res.append(curr_level_values)

        return res

        
        