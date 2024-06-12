import heapq


def solution(A):
    # N = len(A)
    # result = 0
    # for i in range(N):
    #     for j in range(N):
    #         if A[i] == A[j]:
    #             result = max(result, abs(i - j))
    # return result

    min_heaps = {}
    max_heaps = {}

    for i in range(0, len(A)):
        if A[i] not in min_heaps and A[i] not in max_heaps:
            min_heaps[A[i]] = [i]
            heapq.heapify(min_heaps[A[i]])
            max_heaps[A[i]] = [-1 * i]
            heapq.heapify(max_heaps[A[i]])
        else:
            heapq.heappush(min_heaps[A[i]], i)
            heapq.heappush(max_heaps[A[i]], -1 * i)

    max_diff = None
    for num in min_heaps.keys():
        curr_min = heapq.heappop(min_heaps[num])
        curr_max = -1 * heapq.heappop(max_heaps[num])

        if max_diff is None or (curr_max - curr_min) > max_diff:
            max_diff = (curr_max - curr_min)

    return max_diff

if __name__ == "__main__":
    print(solution([4, 6, 2, 2, 6, 6, 1]))