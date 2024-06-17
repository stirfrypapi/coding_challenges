class OrderedStream:
    """
    LC #1656 Design an Ordered Stream
    """

    def __init__(self, n: int):
        # create array with n None strings
        self.arr = [None] * n
        self.ptr_index = 0

    def insert(self, idKey: int, value: str):
        index = idKey - 1
        self.arr[index] = value

        ans = []
        i = self.ptr_index
        while i < len(self.arr) \
                and self.arr[i] is not None:
            ans.append(self.arr[i])
            i += 1

        self.ptr_index = i

        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)


class RandomizedSet:
    """
    LC #380 Insert Delete GetRandom O(1)

    dont delete, just swap it with end value. update indexes
    """

    def __init__(self):
        self.indexes = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.indexes.keys() and len(self.indexes[val]) > 0:
            return False
        self.arr.append(val)
        if val in self.indexes:
            self.indexes[val].append(len(self.arr) - 1)
        else:
            self.indexes[val] = [len(self.arr) - 1]
        return True

    def remove(self, val: int) -> bool:
        """
        [4, 4, 2, 6, 7]
        end: [4, 4, 7, 6]
        {
            4: [0, 1]
            ,2: [2] -> []
            ,6: [3]
            ,7: [4] -> [2]
        }
        delete(2)
        end_val = 7
        end_index = 4
        val_index = 2

        """
        if val not in self.indexes.keys() or len(self.indexes[val]) == 0:
            # value doesnt exist
            return False

        index = self.indexes[val][-1]
        if index == len(self.arr) - 1:
            # remove element from map
            del self.indexes[self.arr[index]][-1]

            # remove element from array
            del self.arr[index]

            # return True
            return True
        else:
            # value exists in map and is not the last element in array
            # swap with end element

            end_val = self.arr[-1]

            val_index = self.indexes[val][-1]

            # swap indexes
            self.indexes[end_val][-1] = val_index

            # delete index
            del self.indexes[val][-1]

            # swap in self.arr
            self.arr[val_index] = end_val

            # delete end element
            del self.arr[-1]

            return True

    def getRandom(self) -> int:
        import random
        random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None


class LRUCache:
    """
    LC #146 LRU Cache
    """
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        # create oldest and newest nodes (dummies)
        # left is oldest, right is newest
        self.left, self.right = Node(0, 0), Node(0, 0)

        # Node(0, 0) <-> Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int):
        if key in self.cache.keys():
            # update LRU cache
            # remove node from linked list
            self.remove(self.cache[key])

            # put node at self.right.prev
            self.insert(self.cache[key])

            # return value
            return self.cache[key].val

        # element does not exist
        return -1

    def put(self, key: int, value: int):
        if key in self.cache:
            self.remove(self.cache[key])

        # create node
        self.cache[key] = Node(key, value)
        # insert into LRU
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # get oldest node
            oldest = self.left.next
            # remove from left of LRU
            self.remove(oldest)
            del self.cache[oldest.key]

    def remove(self, node):
        # remove from linked list
        prev = node.prev
        next_node = node.next

        prev.next = next_node
        next_node.prev = prev

    def insert(self, node):
        # insert to self.right (newest used)
        second_newest = self.right.prev
        second_newest.next = node
        node.next = self.right
        node.prev = second_newest
        self.right.prev = node


class Solution:
    def merge(self, intervals):
        """
        LC #56 Merge Intervals
        sort intervals by tuple[0], then process
        O(n)
        """
        # sort by first element in each tuple
        intervals.sort(key=lambda x: int(x[0]))

        ans = [intervals[0]]
        j = 0

        for i in range(1, len(intervals)):
            curr = intervals[i]

            if curr[0] <= ans[j][1]:
                ans[j][1] = max(ans[j][1], curr[1])
            elif curr[0] > ans[j][1]:
                ans.append(curr)
                j += 1

        return ans

    def decodeString(self, s: str):
        """
        LC #394 Decode String
        2[30[abc]]
        stack: 2, [, 3, 0, [, a, b, c
        2, [, abcabcabcabcabc

        nested loops. process inner [operations] first
        O(n)
        """
        stack = []

        for char in s:
            if char == ']':
                # pop from stack
                # until open bracket
                letters = stack.pop()

                # when at ']', need to calculate the inside before moving on

                # handle substring
                while stack and stack[-1] != '[':
                    # c -> bc -> abc
                    letters = stack.pop() + letters

                stack.pop()  # this will be '['

                nums = stack.pop()

                # handle numbers
                while stack and stack[-1] != '[' and stack[-1].isdigit():
                    # '30'
                    nums = stack.pop() + nums

                # generate multiplied substring, append back to stack
                stack.append(int(nums) * letters)

            elif char == '[':
                stack.append('[')
            else:
                stack.append(char)
        return "".join(stack)

    def inorder_traversal(self, node, ans):
        if node is None:
            return
        self.inorder_traversal(node.left, ans)
        ans.append(int(node.val))
        self.inorder_traversal(node.right, ans)

    def isValidBST(self, root):
        """
        LC #98 Validate BST

        create inorder traversal then check its ordered.
        O(n)
        """
        ans = []
        self.inorder_traversal(root, ans)

        for i in range(1, len(ans)):
            if ans[i] <= ans[i - 1]:
                return False
        return True

    def numIslands(self, grid):
        """
        LC #200 Number of Islands
        """
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        num_islands = 0
        stack = []

        for row_ind in range(0, num_rows):
            for col_ind in range(0, num_cols):
                if grid[row_ind][col_ind] == "1" and \
                        visited[row_ind][col_ind] == 0:
                    num_islands += 1
                    stack.append([row_ind, col_ind])

                while stack:
                    # add all island bits into stack
                    curr_row, curr_col = stack[-1][0], stack[-1][1]

                    stack.pop(-1)

                    # left
                    if curr_col - 1 >= 0 \
                        and visited[curr_row][curr_col-1] == 0 \
                        and grid[curr_row][curr_col-1] == "1":
                        stack.append([curr_row, curr_col-1])
                        visited[curr_row][curr_col-1] = 1
                    # top
                    if curr_row - 1 >= 0 \
                        and visited[curr_row-1][curr_col] == 0 \
                        and grid[curr_row-1][curr_col] == "1":
                        stack.append([curr_row-1, curr_col])
                        visited[curr_row-1][curr_col] = 1
                    # right
                    if curr_col + 1 < num_cols \
                        and visited[curr_row][curr_col+1] == 0 \
                        and grid[curr_row][curr_col+1] == "1":
                        stack.append([curr_row, curr_col+1])
                        visited[curr_row][curr_col+1] = 1
                    # bottom
                    if curr_row + 1 < num_rows \
                        and visited[curr_row+1][curr_col] == 0 \
                        and grid[curr_row+1][curr_col] == "1":
                        stack.append([curr_row+1, curr_col])
                        visited[curr_row+1][curr_col] = 1
        return num_islands

    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        LC #3 Longest Substring without repeating characters

        only move right pointer if next char is not duplicate
        start left at zero, keep moving until substring is unique
        SLIDING WINDOW

        O(n)
        """

        chars = set()
        left_ptr = 0
        right_ptr = 0
        max_len = 0

        # iterate right_ptr until end of string
        while right_ptr < len(s):

            # if new right char is not in set, update max len
            if s[right_ptr] not in chars:
                max_len = max(max_len, right_ptr-left_ptr+1)

                # update set of seen chars
                chars.add(s[right_ptr])

                # update right_ptr
                right_ptr += 1
            else:
                # if new right_ptr char is in set, change left_ptr until
                # it is a unique substring
                while s[right_ptr] in chars and left_ptr < right_ptr:

                    # update char set
                    chars.remove(s[left_ptr])

                    # update left_ptr
                    left_ptr += 1
                #right_ptr += 1

        return max_len

    def exist(self, board, word):
        """
        LC #79 Word Search


        """
        num_rows = len(board)
        num_cols = len(board[0])
        seen_paths = set()

        def dfs(index, curr_row, curr_col):
            # base case for False
            # check for curr_row and curr_col boundaries
            if curr_row < 0 or curr_row >= num_rows or \
                    curr_col < 0 or curr_col >= num_cols:
                return False

            # base case False
            # current letter is not in path
            # or current location has already been visited
            if board[curr_row][curr_col] != word[index] or \
                    (curr_row, curr_col) in seen_paths:
                return False

            # base case for True
            # reached end of word search, found all previous letters
            if index == len(word) - 1:
                return True

            # add location to seen_paths
            seen_paths.add((curr_row, curr_col))

            # recursion for next index
            # left
            res = (dfs(index + 1, curr_row - 1, curr_col)
                   # bottom
                   or dfs(index + 1, curr_row + 1, curr_col)
                   # left
                   or dfs(index + 1, curr_row, curr_col - 1)
                   # right
                   or dfs(index + 1, curr_row, curr_col + 1))

            # remove from paths set when the call stack starts to unravel
            seen_paths.remove((curr_row, curr_col))

            return res

        for curr_row in range(num_rows):
            for curr_col in range(num_cols):

                # search for word, dfs
                if dfs(0, curr_row, curr_col):
                    return True

                # if current location has no valid word search, reset paths set
                seen_paths = set()

        # no word search found
        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.lengthOfLongestSubstring("dvdf"))
