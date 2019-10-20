class Solution(object):
    ###########################################################################
    ###########################################################################
    ######################### CLIMB STAIRS 70 #################################
    ###########################################################################
    ###########################################################################
    def climbStairs(self, n):
        """
        n -> int, number of stairs
        you can only climb 1 or 2 stairs. how many ways to get to top?
        at any step n, steps[n] = steps[n-1] + steps[n-2]
        """
        if n == 1:
            return 1
        steps = [0 for i in range(n)]
        steps[0] = 1
        steps[1] = 2
        for i in range(2, len(steps)):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[-1]

    ###########################################################################
    ###########################################################################
    ######################### COIN CHANGE 322 #################################
    ###########################################################################
    ###########################################################################
    def coinChange(self, coins, amount):
        """
        :param coins: List[int]
        :param amount: int
        :return: int
        """
        # bottom up approach
        ways = [amount+1 for _ in range(amount + 1)]
        ways[0] = 0

        for i in range(1, len(ways)):
            for coin in coins:
                if i - coin > -1:
                    ways[i] = min(ways[i], ways[i-coin] + 1)

        if ways[-1] == amount+1:
            return -1
        return ways[-1]

    ###########################################################################
    ###########################################################################
    ######################### LONGEST INCREASING SUBSEQUENCE 300 ##############
    ###########################################################################
    ###########################################################################
    def lengthOfLIS(self, nums):
        """
        bottom up approach:

        :param nums:
        :return: length of maximum increasing subsequence
        """
        if nums == []:
            return 0

        dp = [1 for _ in nums]

        for j in range(1, len(dp)):
            for i in range(0, j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

    ###########################################################################
    ###########################################################################
    ######################### WORD BREAK 139 ##################################
    ###########################################################################
    ###########################################################################
    def wordBreak(self, s, wordDict):
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True

        for j in range(1, len(dp)):
            for i in range(0, j):
                if dp[i] and s[i:j] in wordDict:

                    dp[j] = True

        return dp[-1]

if __name__ == '__main__':
    s = Solution()

    ###########################################################################
    ###########################################################################
    ######################### CLIMB STAIRS 70 #################################
    ###########################################################################
    ###########################################################################
    print(s.climbStairs(3))

    ###########################################################################
    ###########################################################################
    ######################### COIN CHANGE 322 #################################
    ###########################################################################
    ###########################################################################
    print('Coin change:')
    print(s.coinChange([1, 2 ,5], 11)) # 3
    print(s.coinChange([2], 3)) # -1

    ###########################################################################
    ###########################################################################
    ######################### LONGEST INCREASING SUBSEQUENCE 300 ##############
    ###########################################################################
    ###########################################################################
    print('Longest Increasing Subsequence:')
    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18])) # 4

    ###########################################################################
    ###########################################################################
    ######################### WORD BREAK 139 ##################################
    ###########################################################################
    ###########################################################################
    print('Word Break:')
    print(s.wordBreak('applepenapple', ['pen', 'apple'])) # True
    print(s.wordBreak('leetcode', ['leet', 'code'])) # True