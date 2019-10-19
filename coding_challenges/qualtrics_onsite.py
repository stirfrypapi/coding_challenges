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
            if child_Node.expression == '':
                if root.expression == '+':
                    running_answer += rec(child_Node, running_answer)
                if root.expression == '*':
                    running_answer *= rec(child_Node, running_answer)
            if child_Node.expression != '':
                if root.expression == '+':
                    running_answer += rec(child_Node, 1)
        return running_answer

    if root.expression == '+':
        return rec(root, 0)
    elif root.expression == '*':
        return rec(root, 1)

def wordbreak(word, dictionary):
    # given a word and a list of words (dictionary) return true if the word
    # can be formed by a subset of words in dictionary. false if not

    def rec(word):
        if word in dictionary:
            return True
        if word == "":
            return False
        if len(word) == 1 and word not in dictionary:
            return False
        for i in range(1, len(word)):
            return rec(word[0:i]) and rec(word[i:])

    return rec(word)

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
    """
    +
    | \ \ 
    3  4  5
    """
    multiply = Node()
    multiply.expression = '*'
    multiply_three = Node()
    multiply_three.val = 3
    multiply_two = Node()
    multiply_two.val = 2
    multiply.children = [multiply_three, multiply_two]
    root.children.append(multiply)
    print(evaluate_expression_tree(root)) # expected 18
    """
    +
    | \ \  \ 
    3  4  5 *
           / \ 
          3    2
    """
    print(evaluate_expression_tree(multiply)) # expected 6
    add = Node()
    add.expression = '+'
    six = Node()
    six.val = 6
    multiply = Node()
    multiply.expression = '*'
    multiply.children = [multiply_two, multiply_three]
    add.children = [six, multiply]
    print(evaluate_expression_tree(add)) # expected 12

    print(wordbreak('iamamazing', ['i', 'am', 'amazing']))