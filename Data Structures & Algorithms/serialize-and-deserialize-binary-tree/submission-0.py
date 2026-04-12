# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    """
    preorder + "N" if there is no child node
    """

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ",".join(res)
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(values[self.i])
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()

    def serialize_my(self, root: Optional[TreeNode]) -> str:
        """
        We can convert into 2 strings, lets think about that.
        it's possible to express tree by using inorder traversal and preorder traversal
        
        it's point that if you use only inorder traversal or preorder traversal,
        you cant clarify where it is none child node

        finally, we should return one string, we need to convert 2 strings into 1
        i wanna use "x" and ",". x is used for convert 1 string into 2 string
        "," is used for cutting value for each node.

        It's NOT work when values in tree is not unique
        """
        if not root:
            return "x"

        def inorder_traversal(node: Optional[TreeNode]) -> List[int]:
            res = []
            if node.left:
                res.extend(inorder_traversal(node.left))
            res.append(node.val)
            if node.right:
                res.extend(inorder_traversal(node.right))
            return res 
        
        def preorder_traversal(node: Optional[TreeNode]) -> List[int]:
            res = [node.val]
            if node.left:
                res.extend(preorder_traversal(node.left))
            if node.right:
                res.extend(preorder_traversal(node.right))
            return res

        preorder = preorder_traversal(root)
        inorder = inorder_traversal(root)
        
        preorder_str = ','.join(map(str, preorder))
        inorder_str = ','.join(map(str, inorder))
        
        return preorder_str + "x" + inorder_str
    
    # Decodes your encoded data to tree.
    def deserialize_my(self, data: str) -> Optional[TreeNode]:
        if data == "x":
            return None
            
        preorder_str, inorder_str = data.split("x")
        preorder = list(map(int, preorder_str.split(',')))
        inorder = list(map(int, inorder_str.split(',')))
        
        def rebuild(preorder, inorder):
            if not preorder or not inorder:
                return None
                
            root = TreeNode(preorder[0])
            mid = inorder.index(preorder[0])
            root.left = rebuild(preorder[1:mid+1], inorder[:mid])
            root.right = rebuild(preorder[mid+1:], inorder[mid+1:])
            return root

        return rebuild(preorder, inorder)
        def rebuild(preorder, inorder) -> Optional[TreeNode]:
            pass

        return rebuild(preorder, inorder)
