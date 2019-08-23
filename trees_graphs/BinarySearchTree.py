class BinarySearchTree(object):
    def __init__(self, list):
        return

    ###################################################################################################################
    ###################################################################################################################
    ################################ IS VALID BST? 98 #################################################################
    ###################################################################################################################
    ###################################################################################################################
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: return True
        parents = [root]
        while parents:
            for n in parents:
                if n.left is not None and n.left.val > n.val: return False
                if n.right is not None and n.right.val < n.val: return False
            children = [[n.left, n.right] for n in parents]
            parents = [n for pair in children for n in pair if n]
        return True