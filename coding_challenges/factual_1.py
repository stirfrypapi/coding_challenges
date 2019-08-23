def distance_trucked(readings, end_time):
    distance = 0
    for i in range(0, len(readings)):
        if i == len(readings)-1:
            distance = distance + (end_time/60 - readings[i][0]/60) * readings[i][1]
        else:
            distance = distance + (readings[i+1][0]/60 - readings[i][0]/60) * readings[i][1]
    return distance/60

def x_middle(a, b):
    return (a+b)/2

def y_middle(a, b):
    return (a+b)/2

def midpoint(a, b):
    return [x_middle(a[0], b[0]), y_middle(a[1], b[1])]

def distance(destination, departure):
    x_dist = abs(departure[0] - destination[0])
    y_dist = abs(departure[1] - destination[1])
    return x_dist + y_dist

def closest_point(clients):
    if len(clients) == 0:
        return None
    pt = clients[0]
    for i in range(1, len(clients)):
        pt = midpoint(clients[i], pt)

    total_dist = 0
    for i in range(0, len(clients)):
        total_dist = total_dist + distance(pt, clients[i])

    return int(total_dist)


def mapifyArgument(arg):
    map = {}
    for i in range(0, len(arg)):
        module = arg[i][0]
        dep = arg[i][1]
        if not module in map:
            map[module] = []
        map[module].append(dep)
    return map

def search(dict, item, master_list):
    if item not in dict:
        master_list.append(item)
    else:
        search(dict, item, master_list)

def solution(modulesToBuild, dependencies):
    deps = mapifyArgument(dependencies)
    master_list = []

    for m in modulesToBuild:
        for l in deps[m]:
            search(deps, l, master_list)

    return len(master_list)

def count_keyvals(dict, search_key):
    if search_key in dict:
        

if __name__ == "__main__":
    print(distance_trucked([[0, 90]], 600))
    print(distance_trucked([[0, 90]], 1200))
    print(distance_trucked([[0, 90], [300, 80]], 600))
    print(distance_trucked([[0, 90], [60, 98], [155, 85.5]], 600))

    print(closest_point([[-4, 3], [-2, 1], [1, 0], [3, 2]]))

    print(solution(['abc'], [['abc', '123']])) # expected 2
    print(solution(["abc","def"], [["abc","123"],["abc","456"],["def","456"],["def","789"]])) # expected 5