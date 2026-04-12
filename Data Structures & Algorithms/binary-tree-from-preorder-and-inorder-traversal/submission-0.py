# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    preoder: root-first-oder(root → left → right)
    inoder: root-middle-order(left → root → right) BST's oder
    postoder: root-last-order(left → right → root)
    
    traversal: 巡回(存在するノードのみを記録)
    → 一つのoderのみでは木の構造は定まらない。どのoderも子ノードがない場合に単純に記録をスキップするから
    → 復元するには次のいずれか、inoder + preoderまたは inoder+postoder

    First, I wanto to share meaning of pre-oder and in-oder as you already know
    pre-oder is acces nodes like root, root's left subtree and root's rigth subtree.
    in-oder is acces nodes like root's left subtree, root  and root's rigth subtree.

    Tips for solving:
    1) preoders's first is definitely root. → then get the sub array without root
    2) left side of inoder's root's value is belonged left subtree. right side of inoder's root's value is belonged right subtree.
    3) mid = inorderでのrootの位置 = 左のサブツリーのノード数

    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Pythonでは以下の場合jは含まない、含めたい場合はj+1
        NO: list[i:j]
        OK: list[i:j+1]

        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : mid+1], inorder[:mid]) 
        root.right = self.buildTree(preorder[mid+1:], inorder[mid + 1:])

        return root