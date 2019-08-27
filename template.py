def someFxn(num):
    return num * 5

def commonality(s):
    hashRight = {}
    commonality = 0
    hashC = {}
    for char in s:
        if char not in hashRight:
            hashRight[char] = 1
        else:
            hashRight[char] += 1
    for char in s:
        if char not in hashC:
            hashC[char] = 0
    hashLeft = {}
    for c in s:
        if c not in hashLeft:
            hashLeft[c] = 1
        else:
            hashLeft[c] += 1
        hashRight[c] -= 1
        if hashRight[c] < 0:
            hashRight[c] = 0
        commonality += min(hashRight[c], hashLeft[c])
    return commonality

if __name__ == "__main__":
    print(someFxn(10))
    print(commonality('bbbbaaa'))
    print(commonality('abcdedeara'))
    print(commonality('safaabafsaafs'))