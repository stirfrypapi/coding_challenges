from trees_graphs.Traversal import Traversal
from trees_graphs.Node import NodeBinaryTree

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

if __name__ == "__main__":
    ###################################################################################################################
    ###################################################################################################################
    ############################################ COMPLETE BINARY TREE #################################################
    ###################################################################################################################
    ###################################################################################################################
    c = CompleteBinaryTree([0, 1, 2, 3, 4, 5, 6, 7, 8])
    traversals = Traversal()
    traversals.traverse(c.root, 'inorder')
    traversals.traverse(c.root, 'preorder')
    traversals.traverse(c.root, 'postorder')