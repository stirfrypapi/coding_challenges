from trees_graphs.Node import NodeBinaryTree

class BinaryTree(object):
    def __init__(self, preorder, inorder):
        self.buildTree(preorder, inorder)

    ###################################################################################################################
    ###################################################################################################################
    ################################ CONSTRUCT BINARY TREE FROM PREORDER AND INORDER 105 ##############################
    ###################################################################################################################
    ###################################################################################################################
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = NodeBinaryTree(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root