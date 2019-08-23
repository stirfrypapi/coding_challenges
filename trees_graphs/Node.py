class Node(object):
    def __init__(self, val, neighbors=[]):
        # graph node
        self.val = val
        self.neighbors = neighbors

class NodeBinaryTree(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

if __name__ == "__main__":
    ###################################################################################################################
    ###################################################################################################################
    ####################################### DESERIALIZE AND SERIALIZE BINARY TREE 297 #################################
    ###################################################################################################################
    ###################################################################################################################
    c = Codec()
    root = c.deserialize('#1#2#3#None#None#4#5#None#None#None#None')
    preorder_traversal(root)
    postorder_traversal(root)
    inorder_traversal(root)
    n1 = NodeBinaryTree(1)
    n2 = NodeBinaryTree(2)
    n3 = NodeBinaryTree(3)
    n4 = NodeBinaryTree(4)
    n5 = NodeBinaryTree(5)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    print()
    print(c.serialize(n1))
    print(c.serialize_queue(n1))
    preorder_traversal(c.deserialize(c.serialize(n1)))
