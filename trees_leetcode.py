from node_class import NodeBinaryTree

class Solution(object):
    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None

    ###################################################################################################################
    ###################################################################################################################
    ############################################ MAXIMUM DEPTH BINARY TREE 104 ########################################
    ###################################################################################################################
    ###################################################################################################################
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    ###################################################################################################################
    ###################################################################################################################
    ############################################ IS SAME TREE 100 #####################################################
    ###################################################################################################################
    ###################################################################################################################
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is not None or q is not None:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    ###################################################################################################################
    ###################################################################################################################
    ############################################ INVERT TREE 226 ######################################################
    ###################################################################################################################
    ###################################################################################################################
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        queue = [root]

        while queue:
            node = queue[0]
            queue.pop(0)
            temp = node.left
            node.left = node.right
            node.right = temp
            if node.left is not None: queue.append(node.left)
            if node.right is not None: queue.append(node.right)

        return root





if __name__ == "__main__":
    ###################################################################################################################
    ###################################################################################################################
    ############################################ MAXIMUM DEPTH BINARY TREE 104 ########################################
    ###################################################################################################################
    ###################################################################################################################
    s = Solution()
    # [3,9,20,null,null,15,7]
    n1 = NodeBinaryTree(3)
    n2 = NodeBinaryTree(9)
    n3 = NodeBinaryTree(20)
    n4 = NodeBinaryTree(None)
    n5 = NodeBinaryTree(None)
    n6 = NodeBinaryTree(15)
    n7 = NodeBinaryTree(7)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    print(s.maxDepth(n1))

    ###################################################################################################################
    ###################################################################################################################
    ############################################ IS SAME TREE 100 #####################################################
    ###################################################################################################################
    ###################################################################################################################
