def prefixIsInString(prefix, word):
    if len(prefix) > len(word):
        return False
    for i in range(0, len(prefix)):
        if prefix[i] == word[i]:
            continue
        else:
            return False
    return True


def solution(strings, sources):
    ans = []
    for source in sources: # source = "onetwo"
        source_index = 0 # 0
        for i in range(0, len(strings)): # i=2
            if prefixIsInString(strings[i], source[source_index:]): # ("b", "b")
                source_index += len(strings[i]) # 3
            else:
                ans.append(False)
                break
            if source[source_index:] == "":
                ans.append(True)
                break
            elif i == len(strings)-1:
                ans.append(False)
                break
    return ans


def createArray(n, m):
    ans = []

    for row in range(0, n):
        curr_row = []
        for col in range(0, m):
            curr_row.append(str((row + 1) * (col + 1)))
        ans.append(curr_row)

    return ans


def getFirstNum(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if arr[i][j] != 'X':
                return int(arr[i][j])
    return None


def getMinimumElement(arr):
    running_min = getFirstNum(arr)
    for row in range(0, len(arr)):
        for col in range(0, len(arr[0])):
            if arr[row][col] != 'X' and int(arr[row][col]) < running_min:
                running_min = int(arr[row][col])
    return running_min


def deactivateCellsInRow(arr, row_num):
    col_len = len(arr[0])
    return arr[:row_num - 1] + [['X'] * col_len] + arr[row_num:]


def deactivateCellsInCol(arr, col_num):
    new_arr = []

    for row in range(0, len(arr)):
        new_col = arr[row][:]
        new_col[col_num - 1] = 'X'
        new_arr.append(new_col)

    return new_arr


def solution2(n, m, queries):
    ans = []
    arr = createArray(n, m)

    for query in queries:
        if len(query) == 1 and query[0] == 0:
            ans.append(getMinimumElement(arr))
        elif len(query) == 2 and query[0] == 1:
            arr = deactivateCellsInRow(arr, query[1])
        elif len(query) == 2 and query[0] == 2:
            arr = deactivateCellsInCol(arr, query[1])

    return ans

if __name__ == "__main__":
    print(solution2(3, 4,
                    [[0],
                     [1, 2],
                     [0],
                     [2, 1],
                     [0],
                     [1, 1],
                     [0]]
    ))