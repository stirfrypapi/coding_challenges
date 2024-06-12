def calc(num_wheels):
    arr = [0, 0, 1, 0]
    if num_wheels < 4:
        return arr[num_wheels]
    for i in range(4, num_wheels+1):
        if i % 2 != 0:
            arr.append(0)
        else:
            print(i)
            print(arr)
            arr.append((arr[i]/4) + 1)
    print(arr)
    return arr[num_wheels]

def routes(forward):
    for a, b in forward:
        print(a,b)

if __name__ == "__main__":
    # print(calc(10))
    # print(calc(3))
    # print(calc(2))
    routes([[1,1000], [2, 5000]])