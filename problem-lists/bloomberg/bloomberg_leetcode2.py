from collections import defaultdict


class UndergroundSystem:
    """
    LC #1396 Design an Underground System
    """

    def __init__(self):
        self.checkin = {}
        self.time = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        """
        check in times dict
        {
            "1": ("Flushing", 10)
        }
        """
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        """
        each station's time to travel
        {
            "Flushing": {
                "Grand Central": [5, 10, ...]
                ,"Times Sq": [2, 4, ...]
            }
        }
        """
        # get start station and start time
        startStation, t0 = self.checkin[id]

        # update times dict with time to travel
        self.time[startStation][stationName].append(t - t0)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # O(N), calculate average, lookup in times dict
        t = self.time[startStation][endStation]
        av = sum(t) / len(t)
        return av


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        """
        LC #430 Flatten a Multilevel double Linked List
        """
        if not head:
            return head

        dummy = Node(0, None, None, None)
        curr_end, stack = dummy, [head]

        # DFS
        while stack:
            temp = stack.pop()

            # child goes to top of stack
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)

            curr_end.next = temp
            temp.prev = curr_end
            temp.child = None
            curr_end = temp
        dummy.next.prev = None
        return dummy.next

    def allPathsSourceTarget(self, graph):
        """
        LC #797 All Paths From Source to Target
        """
        paths = []
        stack = [(0, [0])]

        # DFS
        while stack:
            node, path = stack.pop()

            # base case
            # if node is last node in graph, add final path to result
            if node == len(graph) - 1:
                paths.append(path)

            # add every path from current node to neighbor
            for neighbor in graph[node]:
                stack.append((neighbor, path + [neighbor]))

        return paths

    def twoCitySchedCost(self, costs):
        """
        LC #1029 Two City Scheduling

        send everybody to city A
        calculate the refund if each person goes to A instead of B
        send the people with the biggest refund to city B

        [[10, 20], [30, 200], [400, 50], [30, 20]]
        sending everybody to city A = 470
        savings: [10, 170, -350, -10]
        ans = 470 + (-400 + 50) + (20 - 30) = 470 -350 -10 = 110
        """
        refund = []
        min_cost = 0
        half = int(len(costs) / 2)

        for city_a_cost, city_b_cost in costs:
            # negative values = more savings by sending to city b
            refund.append(city_b_cost - city_a_cost)

            min_cost += city_a_cost

        refund.sort()

        for i in range(half):
            # city_a_cost - city_a_cost + city_b_cost
            min_cost += refund[i]

        return min_cost

    def removeDuplicates(self, s, k):
        """
        LC #1209 Remove All Adjacent Duplicates in String II

        s = "abbeeebd", k = 3
        stack = [{a,1}, {b,2}, {e, 3}]
            > [{a,1}, {b,2}]
            > [{a,1}, {b,3}]
            > [{a,1}, {d,1}]
        ans = "ad"
        """
        stack = []

        # build stack one char at a time
        # if char is not repeating, set a new count = 1
        # if char is repeating, set count += 1
        # delete if the count == k
        for char in s:
            if len(stack) == 0:
                stack.append({"char": char, "count": 1})

            elif stack[-1]["char"] != char:
                # set new count
                stack.append({"char": char, "count": 1})

            elif stack[-1]["char"] == char:
                stack[-1]["count"] += 1

                # delete from stack if count == k
                if stack[-1]["count"] == k:
                    stack.pop(-1)

        # build answer based on leftover chars
        ans = ""
        for i in range(0, len(stack)):
            char = stack[i]["char"]
            count = stack[i]["count"]
            ans = ans + (char * count)

        return ans

    def meetingRoomsII(self, intervals):
        """
        LC #919 Meeting Rooms II
        find minimum number of conference rooms required

        [(0, 30), (5,10), (15,20)]

        think about mapping times on a numver line.

        keep a running count of how many meetings are happening at every time
        return the max count
        +1 when meeting starts
        -1 when meeting ends

        sort starting times in one array, end times in another array
        two pointers. if minimum of the two is the start time,
        increment count. start_ptr += 1

        if there is a tie, shift end_ptr += 1
        """
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        running_max, count = 0, 0
        start_ptr, end_ptr = 0, 0

        while start_ptr < len(intervals) and end_ptr < len(intervals):
            if start[start_ptr] < end[end_ptr]:
                # another meeting started
                start_ptr += 1
                # increment count
                count += 1
            else:
                end_ptr += 1
                count -= 1
            running_max = max(running_max, count)

        return running_max

if __name__ == "__main__":
    sol = Solution()
    print(sol.removeDuplicates("deeedbbcccbdaa", 3))