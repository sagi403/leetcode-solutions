# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        output = []
        curr = root
        pre = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if curr.right and curr.right != pre:
                stack.append(curr)
                curr = curr.right
                continue
            output.append(curr.val)
            pre = curr
            curr = None
        return output
            