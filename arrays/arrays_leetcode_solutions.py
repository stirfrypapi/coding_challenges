class Solution(object):
    ###########################################################################
    ###########################################################################
    ######################### TWO SUM 1 #######################################
    ###########################################################################
    ###########################################################################
    def twoSum(self, nums, target):
        """
        :param nums: List
        :param target: int
        :return: indices of two numbers that add to target
        """
        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [i, seen[complement]]
            seen[nums[i]] = i
        return [-1, -1]

if __name__ == "__main__":
    s = Solution()

    ###########################################################################
    ###########################################################################
    ######################### TWO SUM 1 #######################################
    ###########################################################################
    ###########################################################################
    print(s.twoSum([2, 7, 11, 15], 9)) # [2, 7]