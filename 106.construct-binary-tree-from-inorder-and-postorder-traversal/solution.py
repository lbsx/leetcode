# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder or not inorder:
            return None

        root = TreeNode(postorder[-1])
        # print(postorder)
        # print(inorder)
        root_index = inorder.index(root.val)
        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index+1:], postorder[root_index:-1])

        return root
