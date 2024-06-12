def solution(squares):
    ans = ""
    squares_stack = squares
    stack = []
    num_open = 0
    for i in range(0, len(squares_stack)):
        if squares_stack[i] == "[":
            stack.append(("[", i))
            num_open += 1
        elif squares_stack[i] == "]":
            if len(stack) > 0 and stack[0][0] == "[":
                ans += stack[0][0]
                num_open -= 1
                del stack[0]
            elif len(stack) == 0 or stack[-1] != "[":
                ans += "[]"
    count = 0
    for remaining_square in stack:
        ans += remaining_square[0]
        count += 1
    ans += count * "]"
    return ans


if __name__ == "__main__":
    print(solution("]]"))
    print(solution("][[][]]"))