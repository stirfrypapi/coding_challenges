class Node:
    def __init__(self, v=None):
        self.val = v
        self.next = None
        self.isWord = False
        self.child = None


class List:
    def __init__(self):
        self.list = [Node() for i in range(26)]


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.words = set()
        self.root_list = List()
        self.curr_lvl = self.root_list
        self.prev_list = None

    def ind(self, char):
        return ord(char) - 97

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.words.add(word)

        for i in range(len(word)):
            self.curr_lvl.list[self.ind(word[i])] = Node(word[i])
            if i == len(word) - 1:
                self.curr_lvl.list[self.ind(word[i])].isWord = True
            self.prev_list = self.curr_lvl
            self.curr_lvl = self.curr_lvl.list[self.ind(word[i])].child
            self.prev_list.list[self.ind(word[i])].child = self.curr_lvl
            if self.curr_lvl == None and i + 1 < len(word):
                self.curr_lvl = List()
        self.curr_lvl = self.root_list

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        s = word in self.words
        return s

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        start = self.root_list
        curr = start
        for i in range(len(prefix)):
            if curr.list[self.ind(prefix[i])].val != prefix[i]:
                return False
            curr = curr.list[self.ind(prefix[i])].child
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
if __name__ == '__main__':
    t = Trie()
    t.insert('apple')