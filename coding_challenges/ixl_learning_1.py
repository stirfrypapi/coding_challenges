def holes(num):
    map = {1:0, 2:0, 3:0, 5:0, 7:0, 0:1, 4:1, 6:1, 9:1, 8:2}
    num_str = str(num)
    holes = 0
    for c in num_str:
        holes = holes + map[int(c)]
    return holes

def anagram_difference(a, b):
    c = []
    for i in range(len(a)):
        str_a = a[i]
        str_b = b[i]
        if len(str_a) != len(str_b):
            c.append(-1)
        else:
            a_list = [0] * 26
            b_list = [0] * 26
            diffs = 0
            for j in range(len(str_a)):
                a_list[ord(str_a[j]) - 97] += 1
                b_list[ord(str_b[j]) - 97] += 1
            for k in range(0, len(a_list)):
                if a_list[k] != b_list[k]:
                    diffs += abs(a_list[k] - b_list[k])
            c.append(int(diffs/2))
    return c

def countMax(upRight):
    coords = []
    for i in range(0, len(upRight)):
        coords.append(upRight[i].split())

    maxrow = 0
    maxcol = 0
    for i in range(0, len(coords)):
        maxrow = max(int(coords[i][0]), maxrow)
        maxcol = max(int(coords[i][1]), maxcol)

    grid = []
    for i in range(0, maxrow):
        grid.append([0]*maxcol)

    for i in range(0, len(coords)):
        for j in range(0, int(coords[i][0])):
            for k in range(0, int(coords[i][1])):
                grid[j][k] += 1

    maxnum = max(max(x) for x in grid)

    count = 0
    for i in range(0, maxrow):
        for j in range(0, maxcol):
            if grid[i][j] == maxnum:
                count += 1

    return count

def lcm(a, b):
    greater = max(a, b)

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

def reducedFractionSums(expressions):
    from fractions import Fraction
    sums = []
    for e in expressions:
        fracs = e.split('+')
        a = fracs[0].split('/')[0]
        b = fracs[0].split('/')[1]
        c = fracs[1].split('/')[0]
        d = fracs[1].split('/')[1]
        denom = lcm(int(b), int(d))
        a = int((denom/int(b)) * int(a))
        c = int((denom/int(d)) * int(c))
        reduced = Fraction(a+c, denom)
        sums.append(str(reduced.numerator) + '/' + str(reduced.denominator))
    return sums



if __name__ == "__main__":
    print(holes(819))
    print(holes(630))

    print(anagram_difference(['aaac'], ['bbbd'])) # expected 0
    print(anagram_difference(['tea'], ['ates']))  # expected -1
    print(anagram_difference(['tea'], ['toe']))  # expected 1
    print(anagram_difference(['tea', 'tea', 'tea'], ['ate', 'ates', 'toe']))

    print(countMax(["1 4", "2 3", "4 1"])) # expected 1

    print(reducedFractionSums(["722/148+360/176"])) # expected 2818/407