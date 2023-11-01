# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        seen = dict()
        def cleartree(tree):
            if tree is None:
                return
            cleartree(tree.left)
            if tree.val in seen:
                seen[tree.val] += 1
            else:
                seen[tree.val] = 1
            cleartree(tree.right)
        cleartree(curr)
        globalmax = 0
        for val in seen:
            if globalmax < seen[val]:
                globalmax = seen[val]
                result = [val]
            elif globalmax == seen[val]:
                result.append(val)
        return result
