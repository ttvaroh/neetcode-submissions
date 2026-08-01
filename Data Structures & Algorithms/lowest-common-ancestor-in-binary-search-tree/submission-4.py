# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestor = root
        while ancestor:
            val = ancestor.val
            if (p.val < val and q.val < val):
                ancestor = ancestor.left
            elif (p.val > val and q.val > val):
                ancestor = ancestor.right
            else:
                break
        
        return ancestor