def maxDifference(nums):
    """
    :param nums:
    :return: max difference between nums[i] and nums[j] where j < i
    and the difference is >= 0
    """
    max_difference = -1
    min = 9999999
    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]
        elif nums[i] - min > max_difference:
            max_difference = nums[i] - min
    return max_difference


class Node(object):
    def __init__(self, index, predator, name):
        self.name = index
        self.pred = predator
        self.prey = {}

def minimumGroups(predators):
    """
    :param predators: [-1, 8, 6, 0, 7, 3, 8, 9, -1, 6]
    :return:
    """
    pass


def choose(a, b):
    from math import factorial
    return factorial(a) / (factorial(b) * factorial(a - b))


def beautifulSubarrays(a, m):
    odd_nums = set()
    even_nums = set()
    for num in a:
        if num % 2 == 0:
            even_nums.add(num)
        else:
            odd_nums.add(num)
    return int(choose(len(odd_nums), m)) * len(even_nums)


def connectedSum(n, edges):
    nodes = {}
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        if parent not in nodes:
            nodes[parent] = {child: {}}
        else:
            nodes[parent][child] = {}



if __name__ == "__main__":
    print('Max Difference')
    print(maxDifference([7, 1, 2, 5])) # 4
    print(maxDifference([7, 5, 3, 1])) # -1

    print('Beautiful Subarray')
    print(beautifulSubarrays([1, 2, 3, 4, 5], 2))
    # 4 because 4 distince beautiful arrays:
    # [1, 2, 3]
    # [1, 2, 3, 4]
    # [2, 3, 4, 5]
    # [2, 4, 5]