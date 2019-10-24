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
        index is the amount
        ways[i] is ways to make amount
        """
        # bottom up approach
        ways = [amount+1 for _ in range(amount + 1)]
        ways[0] = 0

        for i in range(1, len(ways)):
            for coin in coins:
                if i - coin > -1: # subtract coin from our curr_amount=i
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
        index is everything we need to loop up to right bound
        dp[i] is the lic length
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

    ###########################################################################
    ###########################################################################
    ######################### COMBINATION SUM 4 377 ###########################
    ###########################################################################
    ###########################################################################
    # recursion approach - tle
    """
    def combinationSum4(self, nums, target):
        combinations = 0

        def rec(sum):
            nonlocal combinations
            if sum == target:
                combinations += 1
                return
            if sum > target:
                return
            for a in nums:
                rec(sum + a)

        rec(0)
        return combinations
    """
    def combinationSum4(self, nums, target):
        """
        bottom up approach:
        index is the target
        dp[i] is the # of ways to make target=i
        dy default, only 1 way to get target=0
        """
        dp = [0 for _ in range(target+1)]
        dp[0] = 1

        for i in range(1, len(dp)):
            for j in range(len(nums)):
                if i >= nums[j]:
                # curr_target will be closer to target if we add nums[j]
                    dp[i] += dp[i-nums[j]]
                    # dp[i-nums[j]] is # combinations when target was j less
                    # than curr_target

        return dp[-1]
    ###########################################################################
    ###########################################################################
    ######################### HOUSE ROBBER 198 ################################
    ###########################################################################
    ###########################################################################
    def rob(self, nums):
        """
        rules: you cant rob two adjacent houses. maximize total loot
        index is the house address
        dp[i] is the max loot from houses 0 to i
        recurrence relation: the max loot is max(dp[i-1], dp[i-2]+nums[i])
        :param nums:
        :return: dp[-1]
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]

    ###########################################################################
    ###########################################################################
    ######################### HOUSE ROBBER II 213 #############################
    ###########################################################################
    ###########################################################################
    def rob2(self, nums):
        """
        extension from house robber 1. the houses are in a circle. so, the
        first and last houses are neighboring.
        solution: just split this into two house robber problems:
        one with nums[0:-2] and one with nums[1:]
        :param nums:
        :return:
        """
        if nums == []:
            return 0
        if len(nums) == 1:
            return nums[0]

        nums_zero = nums[0:-1]
        dp_zero = [0 for _ in range(len(nums_zero))]
        dp_zero[0] = nums_zero[0]
        for i in range(1, len(dp_zero)):
            dp_zero[i] = max(dp_zero[i - 1], dp_zero[i - 2] + nums_zero[i])

        nums_one = nums[1:]
        dp_one = [0 for _ in range(len(nums_one))]
        dp_one[0] = nums_one[0]
        for i in range(1, len(dp_one)):
            dp_one[i] = max(dp_one[i - 1], dp_one[i - 2] + nums_one[i])

        return max(dp_one[-1], dp_zero[-1])



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

    ###########################################################################
    ###########################################################################
    ######################### COMBINATION SUM 4 377 ###########################
    ###########################################################################
    ###########################################################################
    print('Combination Sum:')
    print(s.combinationSum4([1, 2, 3], 4))
    print(s.combinationSum4([4, 2, 1], 32))

    ###########################################################################
    ###########################################################################
    ######################### HOUSE ROBBER 198 ################################
    ###########################################################################
    ###########################################################################
    print('House Robber')
    print(s.rob([1, 2, 3, 1]))
    print(s.rob([2,7,9,3,1]))

    ###########################################################################
    ###########################################################################
    ######################### HOUSE ROBBER II 213 #############################
    ###########################################################################
    ###########################################################################
    print('House Robber II')
    print(s.rob2([2, 3, 2]))
    print(s.rob2([1, 2, 3, 1]))