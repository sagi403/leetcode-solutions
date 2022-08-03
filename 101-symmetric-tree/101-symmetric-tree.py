# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = [(root.right, root.left)]
        while stack:
            right, left = stack.pop()
            if not self.checker(right, left):
                return False
            if left:
                stack.append((left.right, right.left))
                stack.append((right.right, left.left))
        return True
            
    def checker(self, right, left):
        if not right and not left:
            return True
        if not right or not left:
            return False
        if right.val != left.val:
            return False
        return True