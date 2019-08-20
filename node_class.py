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

class CompleteBinaryTree(object):
    def __init__(self, list):
        if len(list) == 0:
            return None

        self.root = NodeBinaryTree(list[0])
        self.node_list = [self.root]
        level = 1
        num_parents = 1
        prev_level_start = 0
        prev_level_end = 1
        curr_level_start = prev_level_end
        curr_level_end = curr_level_start + 2 * num_parents
        count = curr_level_start

        while count < len(list):
            while count < len(list) and count < curr_level_end:
                if count % 2 == 1:
                    self.node_list.append(NodeBinaryTree(list[count]))
                    self.node_list[prev_level_start].left = self.node_list[-1]
                elif count % 2 == 0:
                    self.node_list.append(NodeBinaryTree(list[count]))
                    self.node_list[prev_level_start].right = self.node_list[-1]
                    prev_level_start += 1
                count += 1
            level += 1
            num_parents = 2 ** (level-1)
            curr_level_start = curr_level_end
            curr_level_end = curr_level_start + 2 * num_parents

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(str(root.val) + ' ->', end=' ')
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root is not None:
        print(str(root.val) + ' ->', end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(str(root.val) + ' ->', end=' ')

###################################################################################################################
###################################################################################################################
####################################### DESERIALIZE AND SERIALIZE BINARY TREE 297 #################################
###################################################################################################################
###################################################################################################################
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split('#')[1:]
        if len(data) == 0:
            return None
        root = NodeBinaryTree(int(data[0]))
        node_list = [root]
        level = 1
        parents = 2 ** (level-1)
        prev_level_start = 0
        curr_level_start = 1
        curr_level_end = curr_level_start + 2 * parents
        count = curr_level_start

        while count < len(data):
            while count < len(data) and count < curr_level_end:
                if count % 2 == 1:
                    if data[count] == 'None':
                        node_list.append(None)
                        node_list[prev_level_start].left = node_list[-1]
                    else:
                        node_list.append(NodeBinaryTree(int(data[count])))
                        node_list[prev_level_start].left = node_list[-1]
                elif count % 2 == 0:
                    if data[count] == 'None':
                        node_list.append(None)
                        node_list[prev_level_start].right = node_list[-1]
                    else:
                        node_list.append(NodeBinaryTree(int(data[count])))
                        node_list[prev_level_start].right = node_list[-1]
                    prev_level_start += 1
                count += 1
            level += 1
            parents = 2 ** (level-1)
            curr_level_start = curr_level_end
            curr_level_end = 2 * parents

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == "__main__":
    ###################################################################################################################
    ###################################################################################################################
    ############################################ COMPLETE BINARY TREE #################################################
    ###################################################################################################################
    ###################################################################################################################
    c = CompleteBinaryTree([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print('inorder traversal: ')
    inorder_traversal(c.root)
    print()
    print('preorder traversal: ')
    preorder_traversal(c.root)
    print()
    print('postorder traversal: ')
    postorder_traversal(c.root)

    ###################################################################################################################
    ###################################################################################################################
    ############################################ TRAVERSALS ###########################################################
    ###################################################################################################################
    ###################################################################################################################
    n3 = NodeBinaryTree(3)
    n9 = NodeBinaryTree(9)
    n20 = NodeBinaryTree(20)
    n15 = NodeBinaryTree(15)
    n7 = NodeBinaryTree(7)
    n3.right = n9
    n9.left = n20
    n9.right = n7
    n20.left = n15
    print()
    print('preorder traversal 1: ')
    preorder_traversal(n3)
    n3 = NodeBinaryTree(3)
    n9 = NodeBinaryTree(9)
    n20 = NodeBinaryTree(20)
    n15 = NodeBinaryTree(15)
    n7 = NodeBinaryTree(7)
    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7
    print()
    print('preorder traversal 2: ')
    preorder_traversal(n3)
    ###################################################################################################################
    ###################################################################################################################
    ####################################### DESERIALIZE AND SERIALIZE BINARY TREE 297 #################################
    ###################################################################################################################
    ###################################################################################################################
    c = Codec()
    root = c.deserialize('#1#2#3#None#None#4#5')
    print()
    print('preorder traversal desrialized: ')
    preorder_traversal(root)