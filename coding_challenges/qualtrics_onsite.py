"""
Node for expression tree
children -> List[Node]
expression -> char '+', '-', '*', '/', ''
val -> int
"""
class Node(object):
    def __init__(self):
        self.children = []
        self.expression = ''
        self.val = 0

def evaluate_expression_tree(root):
    # given the root of an expression tree,
    # evaluate its answer

    def rec(root, running_answer):
        if root.expression == '':
            return root.val
        for child_Node in root.children:
            if root.expression == '+':
                return running_answer + evaluate_expression_tree(child_Node)
            if root.expression == '-':
                return evaluate_expression_tree(child_Node) - evaluate_expression_tree(root)
            if root.expression == '*':
                return evaluate_expression_tree(child_Node) * evaluate_expression_tree(root)
            if root.expression == '/':
                return evaluate_expression_tree(child_Node) / evaluate_expression_tree(root)

    return rec(root, 0)

def wordbreak(word, dictionary):
    pass


if __name__ == "__main__":
    root = Node()
    root.expression = '+'
    three = Node()
    three.val = 3
    four = Node()
    four.val = 4
    five = Node()
    five.val = 5
    root.children = [three, four, five]
    print(evaluate_expression_tree(root))