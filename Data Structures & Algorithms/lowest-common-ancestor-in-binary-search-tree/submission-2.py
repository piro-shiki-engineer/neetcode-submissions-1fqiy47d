# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    BST's properties

    - right's value is bigger or equals left's value
    - LCA can be a descendant of itself.

    First, we need to search p and q

    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        現在のノードよりも大きいか小さいかがpとqで比較結果が同じならばlcaも更新される
        """
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur


    def lowestCommonAncestor_my(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        p_all_ancestor = self.getAllAncestor(root, p)
        q_all_ancestor = self.getAllAncestor(root, q)
        
        for i in range(min(len(p_all_ancestor), len(q_all_ancestor))):
            if p_all_ancestor[i] == q_all_ancestor[i]:
                lca = p_all_ancestor[i]
        
        return lca


    def getAllAncestor_my(self, root: TreeNode, node: TreeNode) -> List[TreeNode]:
        all_ancestor = []
        while True:
            all_ancestor.append(root)
            if root.val == node.val:
                break
            elif node.val < root.val:
                root = root.left
            else:
                root = root.right
        print(all_ancestor)

        return all_ancestor