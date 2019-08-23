from trees_graphs.Node import NodeBinaryTree

class Traversal(object):
    def traverse(self, root, type):
        l = []
        type_map = {'inorder': 'inorder_traversal',
                    'preorder': 'preorder_traversal',
                    'postorder': 'postorder_traversal'}
        if type not in type_map:
            print('Invalid traversal type')
            return None
        else:
            print(type_map[type] + ':')
            l = getattr(self, type_map[type])(root)
        for n in l:
            if n == None:
                print('None -> ', end=' ')
            else:
                print(str(n) + ' -> ', end=' ')
        print()

    def inorder_traversal(self, root):
        inorder_list = []
        def inorder(root, l):
            if root is not None:
                inorder(root.left, l)
                l.append(root.val)
                inorder(root.right, l)

        inorder(root, inorder_list)
        return inorder_list

    def preorder_traversal(self, root):
        preorder_list = []
        def preorder(root, l):
            if root is not None:
                l.append(root.val)
                preorder(root.left, l)
                preorder(root.right, l)
        preorder(root, preorder_list)
        return preorder_list

    def postorder_traversal(self, root):
        preorder_list = []
        def postorder(root, l):
            if root is not None:
                postorder(root.left, l)
                postorder(root.right, l)
                l.append(root.val)
        postorder(root, preorder_list)
        return preorder_list

if __name__ == "__main__":
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
    t = Traversal()
    t.traverse(n3, 'inorder')
    t.traverse(n3, 'preorder')
    t.traverse(n3, 'postorder')
    n3 = NodeBinaryTree(3)
    n9 = NodeBinaryTree(9)
    n20 = NodeBinaryTree(20)
    n15 = NodeBinaryTree(15)
    n7 = NodeBinaryTree(7)
    n3.left = n9
    n3.right = n20
    n20.left = n15
    n20.right = n7
    t.traverse(n3, 'inorder')
    t.traverse(n3, 'preorder')
    t.traverse(n3, 'postorder')