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
    print()
    print('inorder traversal: ')
    def inorder(root):
        if root is not None:
            inorder(root.left)
            print(str(root.val) + ' ->', end=' ')
            inorder(root.right)
    inorder(root)

def preorder_traversal(root):
    print()
    print('preorder traversal: ')
    def preorder(root):
        if root is not None:
            print(str(root.val) + ' ->', end=' ')
            preorder(root.left)
            preorder(root.right)

    preorder(root)

def postorder_traversal(root):
    print()
    print('postorder traversal: ')
    def postorder(root):
        if root is not None:
            postorder(root.left)
            postorder(root.right)
            print(str(root.val) + ' ->', end=' ')
    postorder(root)
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
        if root is None: return None
        level = [root]
        data = '#{}'.format(str(root.val))
        while level:
            children = [ [n.left, n.right] for n in level]
            for pair in children:
                for n in pair:
                    add = '#{}'.format(str(n.val)) if n else '#None'
                    data += add
            level = [n for pair in children for n in pair if n]
        return data

    def serialize_queue(self, root):
        # uses queue instead
        if root is None: return None
        queue = [root]
        data = ''
        while queue:
            n = queue[0]
            queue.pop(0)
            add = '#{}'.format(str(n.val)) if n else '#None'
            data += add
            if n is not None: queue.append(n.left)
            if n is not None: queue.append(n.right)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or data == '[]' or data == '':
            return None
        data = data.split('#')[1:]
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
                        # node_list.append(None)
                        node_list[prev_level_start].left = None
                    else:
                        node_list.append(NodeBinaryTree(int(data[count])))
                        node_list[prev_level_start].left = node_list[-1]
                elif count % 2 == 0:
                    if data[count] == 'None':
                        # node_list.append(None)
                        node_list[prev_level_start].right = None
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
    inorder_traversal(c.root)
    preorder_traversal(c.root)
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
    preorder_traversal(n3)
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
