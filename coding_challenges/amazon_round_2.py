def countPairs(numCount, ratingValues, target):
    dict = {}
    pairs = {}
    for r in ratingValues:
        complement = target - r
        if complement not in dict:
            dict[r] = complement
        elif complement in dict:
            pairs[r] = complement
    return len(pairs.keys())

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def isSameTree(p, q):
    """
    :type p: Node
    :type q: Node
    :rtype: bool
    True if roots p and q are same tree. False otherwise.
    """
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

def isSubtree(root1, root2):
    """
    :type s: Node
    :type t: Node
    :rtype: bool
    Return 1 if root2 is subtree in root1 tree. Otherwise return -1.
    """
    queue = [root1]
    while queue:
        n = queue[0]
        queue.pop(0)
        if n.val == root2.val and isSameTree(n, root2):
            return 1
        else:
            if n.left is not None:
                queue.append(n.left)
            if n.right is not None:
                queue.append(n.right)
    return -1

if __name__ == "__main__":
    print(countPairs(10, [10, 3, 5, 7, 2, 8, 9, 6, 1, 4], 7))
