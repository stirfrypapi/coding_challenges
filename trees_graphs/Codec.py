from trees_graphs.Traversal import Traversal
from trees_graphs.Node import NodeBinaryTree
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
    ####################################### DESERIALIZE AND SERIALIZE BINARY TREE 297 #################################
    ###################################################################################################################
    ###################################################################################################################
    c = Codec()
    t = Traversal()
    root = c.deserialize('#1#2#3#None#None#4#5#None#None#None#None')
    t.traverse(root, 'preorder')
    t.traverse(root, 'postorder')
    t.traverse(root, 'inorder')
    n1 = NodeBinaryTree(1)
    n2 = NodeBinaryTree(2)
    n3 = NodeBinaryTree(3)
    n4 = NodeBinaryTree(4)
    n5 = NodeBinaryTree(5)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    print(c.serialize(n1))
    print(c.serialize_queue(n1))
    t.traverse(c.deserialize(c.serialize(n1)), 'preorder')
