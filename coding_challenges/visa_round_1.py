
def get_times(arr):
    ans = [arr[0]]
    for i in range(1, len(arr)):
        temp = [arr[i][0], arr[i][1] - arr[i-1][1]]
        ans.append(temp)
    return ans

def get_total_times(arr):
    ans = {}
    for a in arr:
        if a[0] not in ans:
            ans[a[0]] = a[1]
        else:
            ans[a[0]] = max(a[1], ans[a[0]])
    return ans

def slowestKey(keyTimes):
    import operator
    times = get_times(keyTimes)
    total_times = get_total_times(times)
    return chr(max(total_times.items(), key=operator.itemgetter(1))[0]+97)


def expand_ranges(first, last):
    ans = []
    for f, l in zip(first,last):
        ans.append([f,l])
    return ans

def sort_by_dates(arr):
    ans = {}
    for a in arr:
        if a[0] not in ans:
            ans[a[0]] = [a[1]]
        else:
            ans[a[0]].append(a[1])
    return ans

def countMeetings(firstDay, lastDay):
    num = 0
    dates_taken = set()

    ans = []
    lens = []
    for f, l in zip(firstDay, lastDay):
        if f == l:
            num += 1
            dates_taken.add(f)
        else:
            ans.append([f, l])
            lens.append([f-l+1, len(ans)-1])

    # sort by length and index from ans
    lens.sort()
    for l in lens:
        f, l = ans[l[1]]
        i = f
        while i in dates_taken and i < l+1:
            i += 1
        if i < l+1:
            dates_taken.add(i)
            num += 1

    return num


def findLIS(s):
    num = len(s)
    dp = [1 for _ in range(num)]

    for i in range(1, num):
        for j in range(0, i):
            if dp[i] < dp[j] + 1 and s[i] > s[j]:
                dp[i] = dp[j] + 1

    return max(0, max(dp))

def get_position(num, arr):
    for i in range(0, len(arr)):
        if arr[i] >= num:
            return i - 1
    return len(arr)-1

def get_left_deletes(pos, arr):
    return pos + 1

def get_right_deletes(num, pos, arr):
    i = pos
    while i+1 < len(arr) and arr[i+1] == num:
        i += 1
    return len(arr) - i - 1

def get_ops(num, pos, arr):
    left_dels = get_left_deletes(pos, arr)
    right_dels = get_right_deletes(num, pos, arr)

    if left_dels < right_dels:
        return left_dels + 1 + left_dels
    return right_dels + 1 + right_dels

def insert(num, pos, arr):
    if pos == len(arr) - 1:
        arr.append(num)
    elif pos == -1:
        arr = [num] + arr[0:]
    else:
        arr = arr[0:pos+1] + [num] + arr[pos+1:]
    return arr

def minimumOperations(numbers):
    running_num_ops = 2
    ans_list = [numbers[0], numbers[1]]
    ans_list.sort()

    numbers = numbers[2:]
    for num in numbers:
        pos = get_position(num, ans_list)
        ops = get_ops(num, pos, ans_list)
        running_num_ops += ops
        ans_list = insert(num, pos, ans_list)

    return running_num_ops


if __name__ == "__main__":
    # print(slowestKey([[0,2], [1,3], [0,7]]))
    # print(countMeetings([1,10,11], [11,10,11]))
    # print(countMeetings([1, 1, 2], [1, 2, 2]))
    # print(findLIS([1, 2, 2, 3, 1, 6]))
    # print(minimumOperations([10, 6, 2, 3, 7, 1, 2]))
    # print(minimumOperations([2, 19, 10, 1, 6, 13, 6, 6, 15, 12]))
    print(minimumOperations([9, 8, 4, 9, 28, 21, 24, 18, 29, 25, 9, 3, 19, 5, 3]))
    # print(get_position(10, [2]))
    # [10, 6, 2, 3, 7, 1, 2]