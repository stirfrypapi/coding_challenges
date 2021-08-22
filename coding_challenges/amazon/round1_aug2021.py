import math
import heapq

def get_distance(restLocation):
    x = restLocation[0]
    y = restLocation[1]
    return math.sqrt(x * x + y * y)


def findRestaurants(allLocations, numRestaurants):
    # Write your code here
    allDistances = []
    for i in range(0, len(allLocations)):
        location = allLocations[i]
        allDistances.append([i, get_distance(location)])

    allDistances.sort(key=lambda x: x[1])

    closestRestaurants = []
    for i in range(0, numRestaurants):
        restaurantIndex = allDistances[i][0]
        closestRestaurants.append(allLocations[restaurantIndex])

    return closestRestaurants

# def findRestaurants(allLocations, numRestaurants):
#     allDistancesHeap = []
#
#     for i in range(0, len(allLocations)):
#         location = allLocations[i]
#         heap_element = [get_distance(location), location[0], location[1]]
#
#         # push new element to heap
#         heapq.heappush(allDistancesHeap, heap_element)
#
#         # pop largest element from heap if longer than numRestaurants
#         if len(allDistancesHeap) == numRestaurants+1:
#             heapq.heappop(allDistancesHeap)
#
#     return [(x,y) for (distance, x, y) in allDistancesHeap]


def getTotalMemory(foreground, background):
    return foreground[1] + background[1]

def applicationPairs(deviceCapacity, foregroundAppList, backgroundAppList):
    currentMaxMemory = 0
    indexes = []
    for i in range(0, len(foregroundAppList)):
        foreground = foregroundAppList[i]
        for j in range(0, len(backgroundAppList)):
            background = backgroundAppList[j]
            totalMemory = getTotalMemory(foreground, background)
            if totalMemory > currentMaxMemory and totalMemory <= deviceCapacity:
                indexes = [[foreground[0],background[0]]]
                currentMaxMemory = totalMemory
            elif totalMemory == currentMaxMemory:
                indexes.append([foreground[0],background[0]])
    return indexes

if __name__ == "__main__":
    #print(findRestaurants([[1,2],[3,4],[1,-1]], 2))
    print(findRestaurants([[1, 2], [2, 1], [3, 6], [5, 8], [6, 3], [2, 4], [2, 3], [6, 9], [3, 10], [9, 10]],
                          5)) # [[1, 2], [2, 1], [2, 3], [2, 4], [3, 6]]
    # print(applicationPairs(10, [[1,3],[2,5],[3,7],[4,10]],
    #                        [[1,2],[2,3],[3,4],[4,5]])) #[[2,4],[3,2]])
    # print(applicationPairs(20,
    #                        [[1,8],[2,7],[3,14]],
    #                        [[1,5],[2,10],[3,14]]))