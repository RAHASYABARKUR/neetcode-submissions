# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(main, sub):
            if not main:
                return False
            
            # If current roots match, check full subtree
            if main.val == sub.val:
                if sameTree(main, sub):
                    return True
            
            # Otherwise search deeper
            return dfs(main.left, sub) or dfs(main.right, sub)

        def sameTree(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val != b.val:
                return False
            return sameTree(a.left, b.left) and sameTree(a.right, b.right)

        return dfs(root, subRoot)

'''
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs (main, sub):
            if not sub:
                return True
            if not main:
                return False
            elif main.val == sub.val:
                return dfs(main.left,sub.left) and dfs(main.right,sub.right)
            return dfs(main.left,sub) or dfs(main.right,sub)
            #return False
        return dfs(root,subRoot)'''