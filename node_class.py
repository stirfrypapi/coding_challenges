class Node(object):
    def __init__(self, val, neighbors=[]):
        # graph node
        self.val = val
        self.neighbors = neighbors

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class BinaryTree(object):
#     def __init__(self, list):
#         node_list = []
#         for l in list:
#             n = NodeBinaryTree(l)
#             node_list.append(n)
#
#         for i in range(0, len()):
