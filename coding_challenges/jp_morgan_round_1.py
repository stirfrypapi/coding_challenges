def sum_of_square(num):
    """
    :param num: int
    :return: the sum of squares or each digit
    """
    running_sum = 0
    for i in str(num):
        running_sum += int(i)**2
    return running_sum


def is_happy_number(num):
    """
    returns 1 if num is happy number
    otherwise, returns 0
    :param num: int
    :return: 1 or 0
    """
    seen = set()
    if num == 1:
        return 1

    seen.add(num)
    num = sum_of_square(num)
    while num != 1:
        num = sum_of_square(num)
        if num in seen:
            return 0
        seen.add(num)
    return 1


def valid_parenthesis(input):
    """
    return false if input does not have valid parenthesis (eg ([)])
    return true if valid (eg [()()])
    :param input: string
    :return: boolean True or False
    """
    # first in last out - think a stack of plates
    # append to add to back
    # pop by pop(-1)
    stack = []

    opens = {'[', '(', '{'} # all open parenthesis
    closes = {']', ')', '}'} # all closing parenthesis

    # trading memory for faster lookup
    matchings = {'[': ']',
                 '(': ')',
                 '{': '}'}

    for bracket in input:
        if bracket in opens:
            # keep track of opening brackets
            stack.append(bracket)
        if bracket in closes:
            if len(stack) == 0:
                # return false if we get to a closing parenthesis
                # and there aren't any open parenthesis
                return False
            # the top of the stack must be the opening for the current
            # closing bracket
            last_open = stack.pop(-1)
            if matchings[last_open] != bracket:
                return False

    # return true only if the stack is empty and there are no more parenthesis
    # to look at in the input
    return len(stack) == 0



if __name__ == "__main__":
    print(sum_of_square(0))
    print(is_happy_number(7))
    print(is_happy_number(22))

    print('Valid Parenthesis')
    print(valid_parenthesis('{[()]}')) # true
    print(valid_parenthesis('([)]')) # false
    print(valid_parenthesis('')) # true
    print(valid_parenthesis('[()()]'))  # true
    print(valid_parenthesis('['))  # false
    print(valid_parenthesis(']'))  # false
    print(valid_parenthesis(']]]'))  # false