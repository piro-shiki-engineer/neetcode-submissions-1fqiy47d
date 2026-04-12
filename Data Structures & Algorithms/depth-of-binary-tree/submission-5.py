# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    traversing: 横断する
    baseケースつまり参照しているノードが場合は加算しない

    それぞれのSubTreeでDFSをおこなって、最終的により深い部分木の結果を足していく
    ノードがあれば深さは1が加算
    Recursive DFS Depth First Search 
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: Best O(N), Worse O(N) Because it's not balanced Binary Tree
        Space Complexity: O(1)
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        """
        without using Recusive
        You can use the stack. → Because emulating calll stack the recusive call stack
        再帰コールスタックをエミュレートするため

        stackにはノードのみ入れるのではなく各ノードのlevelも同時に格納する。
        """
        # 深さはnodeがなければ更新されないから再帰のベースケースは不要
        # if not root:
        #     return 0
        
        stack = [(root, 1)]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node: 
                res = max(res, depth)
                stacj
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth+1])
        return res

    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
        """
        Space
        BFS Breath First Search on a tree is basically level order taraversal 
        各階層をごとにサーチする探索手法→ counting level 
        Queue 
        初期状態: [root] 
        dequeからpop rootを探索して root.left, root.rightをque
        queueがからになるまでこれを繰り返す
        """
        if not root:
            return 0
        
        level = 0
        q = deque([root]) # initialize

        while q: # unti queue is emply
            for i in ragne(len(q)):
                node = q.popleft()
                if node.left:
                    q.appen(node.left)
                
                if node.right:
                    q.appen(node.right)
                
            level += 1 # count up 1 if queue is not emtpy
        
        return level# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    traversing: 横断する
    baseケースつまり参照しているノードが場合は加算しない

    それぞれのSubTreeでDFSをおこなって、最終的により深い部分木の結果を足していく
    ノードがあれば深さは1が加算
    Recursive DFS Depth First Search 
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: Best O(N), Worse O(N) Because it's not balanced Binary Tree
        Space Complexity: O(1)
        """
        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

    def maxDepth_iterative(self, root: Optional[TreeNode]) -> int:
        """
        without using Recusive
        You can use the stack. → Because emulating calll stack the recusive call stack
        再帰コールスタックをエミュレートするため

        stackにはノードのみ入れるのではなく各ノードのlevelも同時に格納する。
        """
        # 深さはnodeがなければ更新されないから再帰のベースケースは不要
        # if not root:
        #     return 0
        
        stack = [(root, 1)]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node: 
                res = max(res, depth)
                stacj
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth+1])
        return res

    def maxDepth_BFS(self, root: Optional[TreeNode]) -> int:
        """
        Space
        BFS Breath First Search on a tree is basically level order taraversal 
        各階層をごとにサーチする探索手法→ counting level 
        Queue 
        初期状態: [root] 
        dequeからpop rootを探索して root.left, root.rightをque
        queueがからになるまでこれを繰り返す
        """
        if not root:
            return 0
        
        level = 0
        q = deque([root]) # initialize

        while q: # unti queue is emply
            for i in ragne(len(q)):
                node = q.popleft()
                if node.left:
                    q.appen(node.left)
                
                if node.right:
                    q.appen(node.right)
                
            level += 1 # count up 1 if queue is not emtpy
        
        return level