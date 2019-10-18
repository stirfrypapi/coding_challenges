def maxLCS(s):
    # get initial count of each letter in s
    count = [0 for i in range(26)]
    for letter in s:
        count[ord(letter) - ord('a')] += 1

    current_commonality = 0
    running_max = 0
    for letter in s:
        current_index = ord(letter) - ord('a')
        if count[current_index] > 1:
            # since the count of the current letter is greater than 1,
            # let's split at the current index because this will add
            # one to the commonality
            current_commonality += 1
            # now that we've accounted for this scenario, subtract 2 from the
            # count so that we don't double count this case
            count[current_index] -= 2
        elif count[current_index] == 0:
            # counted too far, so go back one
            current_commonality -= 1
        else:
            # we only enter here when the count is 1
            # doesn't matter which side this letter is on, so let's just
            # subtract 1
            count[current_index] -= 1
        # keep a running max of the commonality
        running_max = max(current_commonality, running_max)
    return running_max


def count_live_neighbors(grid, neighbors):
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            count = 0
            if i-1 > -1 and j-1 > -1 and grid[i-1][j-1] == 1:
                count += 1 # top left
            if i-1 > -1 and grid[i-1][j] == 1:
                count += 1 # above
            if i-1 > -1 and j+1 < cols and grid[i-1][j+1] == 1:
                count += 1 # top right
            if j+1 < cols and grid[i][j+1] == 1:
                count += 1 # right
            if i+1 < rows and j+1 < cols and grid[i+1][j+1] == 1:
                count += 1 # bottom right
            if i+1 < rows and grid[i+1][j] == 1:
                count += 1 # bottom
            if i+1 < rows and j-1 > -1 and grid[i+1][j-1] == 1:
                count += 1 # bottom left
            if j-1 > -1 and grid[i][j-1] == 1:
                count += 1 # left
            neighbors[i][j] = count


def change_grid(grid, neighbors, rules):
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if neighbors[i][j] in rules:
                grid[i][j] = 1
            else:
                grid[i][j] = 0


def gridGame(grid, k, rules):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = [[0 for _ in range(cols)] for _ in range(rows)]

    set_rules = set()
    for i in range(len(rules)):
        if rules[i] == 'alive':
            set_rules.add(i)

    for i in range(k):
        count_live_neighbors(grid, neighbors)
        change_grid(grid, neighbors, set_rules)
    return grid

if __name__ == "__main__":
    print(maxLCS('abcdedeara'))
    print(maxLCS('aabb'))

    grid = [
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    rules = [
        'dead',
        'alive',
        'dead',
        'dead',
        'dead',
        'dead',
        'dead',
        'dead',
        'dead',
    ]
    print(gridGame(grid, 1, rules))