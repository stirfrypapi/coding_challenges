import heapq
import math
import random

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class RandomizedSet:
    # https://leetcode.com/problems/insert-delete-getrandom-o1/
    def __init__(self):
        self.data = []
        self.data_dict = {}

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data.append(val)
        self.data_dict[val] = len(self.data)-1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        index = self.data_dict[val]
        end_val = self.data[-1]
        self.data_dict[end_val] = index
        self.data[index] = end_val
        del self.data_dict[val]
        self.data.pop(-1)
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.data = {}

    def _add(self, node):
        old = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.next = old
        old.prev = node
        node.prev = self.head

    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.data.keys():
            # update cache
            accessed_node = self.data[key]
            self._remove(accessed_node)
            self._add(accessed_node)
            return self.data[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            # update value
            self.data[key].val = value
            curr_node = self.data[key]
            self._remove(curr_node)
            self._add(curr_node)
        elif len(self.data.keys()) < self.capacity:
            # add new node
            new_node = Node(key, value)
            self.data[key] = new_node
            self._add(new_node)
        elif len(self.data.keys()) == self.capacity:
            oldest_node = self.tail.prev
            self._remove(oldest_node)
            del self.data[oldest_node.key]
            new_node = Node(key, value)
            self.data[key] = new_node
            self._add(new_node)



class Solution:
    def decodeString(self, s: str) -> str:
        """
        2[3[abc]]
        stack: 2, [, 3, [, abc
        """
        stack = []

        for char in s:
            if char == ']':
                # pop from stack
                # until open bracket
                letters = stack.pop()
                while stack and stack[-1] != '[':
                    letters = stack.pop() + letters
                stack.pop()
                nums = stack.pop()
                while stack and stack[-1] != '[' and stack[-1] >= '0' and stack[-1] <= '9':
                    nums = stack.pop() + nums
                stack.append(int(nums) * letters)
            elif char == '[':
                stack.append('[')
            else:
                stack.append(char)
        return "".join(stack)

    def longestPalindrome(self, s):
        # https://leetcode.com/problems/longest-palindromic-substring/
        start, end = 0, 0
        max_len = 0

        for i in range(len(s)):
            len1 = self._expandAroundCenter(s, i, i)
            len2 = self._expandAroundCenter(s, i, i+1)
            len_curr = max(len1, len2)
            if len_curr > max_len:
                max_len = len_curr
                start = i - int((len_curr-1)/2)
                end = i + int(len_curr/2)
        return s[start: end+1]

    def _expandAroundCenter(self, s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    def minMeetingRooms(self, intervals):
        # https://leetcode.com/problems/meeting-rooms-ii/
        if len(intervals) == 0:
            return 0

        intervals = sorted(intervals, key=lambda x: x[0])
        rooms = [intervals[0][1]]
        heapq.heapify(rooms)

        for i in range(1, len(intervals)):
            if intervals[i][0] >= rooms[0]:
                # if end time of new meeting is greater than or equal to
                # most recently open room
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])

        return len(rooms)

    def numIslands(self, grid):
        # https://leetcode.com/problems/number-of-islands/
        rows = len(grid)
        cols = len(grid[0])
        num_islands = 0

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        queue = []
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == "1":
                    queue.append([i, j])
                    num_islands += 1
                    while queue:
                        pos = queue.pop()
                        row, col = pos[0], pos[1]
                        if (row + 1) < rows and not visited[row + 1][col] and grid[row + 1][col] == "1":
                            visited[row+1][col] = 1
                            queue.append([row+1, col])
                        if (row - 1) > -1 and not visited[row - 1][col] and grid[row - 1][col] == "1":
                            visited[row-1][col] = 1
                            queue.append([row-1, col])
                        if (col - 1) > -1 and not visited[row][col - 1] and grid[row][col - 1] == "1":
                            visited[row][col-1] = 1
                            queue.append([row, col-1])
                        if (col + 1) < cols and not visited[row][col + 1] and grid[row][col + 1] == "1":
                            visited[row][col+1] = 1
                            queue.append([row, col+1])
        return num_islands

    def merge(self, intervals):
        # https://leetcode.com/problems/merge-intervals/

        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])

        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])

        return ans

    def twoSum(self, nums, target):
        # https://leetcode.com/problems/two-sum/
        nums_dict = {}

        for i in range(0, len(nums)):
            comp = nums[i]
            if comp in nums_dict:
                nums_dict[comp].append(i)
            else:
                nums_dict[comp] = [i]

        for i in range(0, len(nums)):
            comp = target - nums[i]
            if comp in nums_dict:
                for ind in nums_dict[comp]:
                    if ind != i:
                        return [i, ind]
        return None

    def split_helper(self, domainName: str):
        ans = [domainName]
        prev_period_index = domainName.index(".", 0)
        i = prev_period_index + 1
        while i < len(domainName):
            if domainName[i] == ".":
                ans.append(domainName[prev_period_index + 1:])
                prev_period_index = i
            i += 1
        return ans

    def isNotDigit(self, char):
        if char >= '0' and char <= '9':
            return False
        return True

    def calculate(self, s: str) -> int:
        if s == "":
            return 0
        stack = []  # 6,
        currentNumber = 0
        operation = '+'  # *

        for i in range(0, len(s)):
            currentChar = s[i]
            if currentChar >= '0' and currentChar <= '9':
                if currentNumber == 0:
                    currentNumber = int(currentChar)  # 2
                else:
                    currentNumber = int(currentChar + str(currentNumber))
            if (self.isNotDigit(currentChar) and currentChar != " ") \
                    or i == len(s)-1:
                if operation == '-':
                    stack.append(-1 * currentNumber)
                elif operation == '+':
                    stack.append(currentNumber)
                elif operation == '*':
                    num = stack.pop(-1)
                    stack.append(num * currentNumber)
                elif operation == '/':
                    num = stack.pop(-1)
                    stack.append(int(num / currentNumber))
                operation = currentChar
                currentNumber = 0
        return sum(stack)

if __name__ == "__main__":
    s = Solution()
    # print(s.twoSum([3,3], 6))
    #
    # lru = LRUCache(2)
    # lru.put(2, 1)
    # lru.put(2, 2)
    # print(lru.get(2))
    # lru.put(1, 1)
    # lru.put(4, 1)
    # print(lru.get(2))
    # print(s.merge([[4, 8], [2, 7], [4, 6], [4, 9]]))
    # print(s.numIslands([["1","1","1","1","0"],
    #                     ["1","1","0","1","0"],
    #                     ["1","1","0","0","0"],
    #                     ["0","0","0","0","0"]
    # ]))
    # print(s.minMeetingRooms([[0,30],[5,10],[15,20]]))
    # print(s.longestPalindrome("bb"))
    # print(s.decodeString("3[a]2[bc]"))
    print(s.calculate(" 3+2*2 "))