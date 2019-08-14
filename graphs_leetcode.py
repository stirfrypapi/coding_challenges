from node_class import Node

class Solution(object):

    ###################################################################################################################
    ###################################################################################################################
    ############################################ DEEP COPY GRAPH 133 ##################################################
    ###################################################################################################################
    ###################################################################################################################

    def clone_graph_133(self, node):
        '''
        Task: deep copy a graph. each node has a value and a list of neighboring nodes
        BFS Approach:
            1. base case: if the node is empty, return None
            2. keep a dictionary w keys = original nodes & values = copies of nodes
            3. keep a queue of nodes to copy
            4. iterate through queue. pop each node, make a copy of it and its neighbors, add to dictionary to keep track
            5. return first node
        '''
        if node is None:
            return
        head_copy = Node(node.val, [])
        dic = {node: head_copy}
        queue = [node]

        while queue:
            node = queue[0]
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighbor_copy = Node(neighbor.val)
                    dic[neighbor] = neighbor_copy
                    dic[node].neighbors.append(neighbor_copy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
            queue.pop(0)
        return head_copy

    def dfs(self, dic, node):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighbor_copy = Node(neighbor.val)
                dic[neighbor] = neighbor_copy
                dic[node].neighbors.append(neighbor_copy)
                self.dfs(dic, neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])

    def clone_graph_133_DFS(self, node):
        if node is None:
            return
        head_copy = Node(node.val, [])
        dic = {node: head_copy}
        self.dfs(dic, node)
        return head_copy

    ###################################################################################################################
    ###################################################################################################################
    ############################################ DETECT CYCLE 207 #####################################################
    ###################################################################################################################
    ###################################################################################################################

    def edges_to_adj_list(self, num_vertices, edges):
        adj_list = [[] for _ in range(num_vertices)]

        for pair in edges:
            to, from_dest = pair
            adj_list[from_dest].append(to)

        return adj_list

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool

        Task: detect if there is a cycle in the graph. If there is, return false. else, return true
        BFS:
            1. compute indegrees for each vertex. initialize number of visited nodes to 0
            2. add all nodes w indegree = 0 to a queue
            3. pop from queue
                i. count++
                ii. decrease neighbor indegree by 1
                iii. if neighbor indegree = 0, add to queue
            4. repeat 3. until queue is empty
            5. if count of visited nodes != # nodes then there is cycle (false). else no cycle (true)
        """
        indegrees = [0 for _ in range(numCourses)]
        visited_nodes = 0
        queue = []
        adj_list = self.edges_to_adj_list(numCourses, prerequisites)
        for pair in prerequisites:
            upperlevel, prereq = pair
            indegrees[upperlevel] += 1

        for i in range(0, len(indegrees)):
            if indegrees[i] == 0:
                queue.append(i)

        while queue:
            visited_nodes += 1
            node = queue[0]
            queue.pop(0)
            for neighbor in adj_list[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return (visited_nodes == numCourses)

    ###################################################################################################################
    ###################################################################################################################
    ############################################ PACIFIC ATLANTIC WATER FLOW 417 ######################################
    ###################################################################################################################
    ###################################################################################################################
    def bfs_from_ocean(self, matrix, queue, visited):
        rows = len(matrix)
        cols = len(matrix[0])
        while queue:
            x, y = queue[0]
            queue.pop(0)
            curr_val = matrix[x][y]
            visited[x][y] = 1
            # right
            if y + 1 < cols and matrix[x][y + 1] >= curr_val and visited[x][y + 1] == 0:
                visited[x][y + 1] = 1
                queue.append([x, y + 1])
            # bottom
            if x + 1 < rows and matrix[x + 1][y] >= curr_val and visited[x + 1][y] == 0:
                visited[x + 1][y] = 1
                queue.append([x + 1, y])
            # left
            if y - 1 >= 0 and matrix[x][y - 1] >= curr_val and visited[x][y - 1] == 0:
                visited[x][y - 1] = 1
                queue.append([x, y - 1])
            # top
            if x - 1 >= 0 and matrix[x - 1][y] >= curr_val and visited[x - 1][y] == 0:
                visited[x - 1][y] = 1
                queue.append([x - 1, y])
        return visited

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]

        Task: for every point in matrix, BFS to see if point can travel to pacific (top and left border) and atlantic
        (bottom and right border). Point can travel to place with equal or lower value
        """
        if len(matrix) == 0:
            return
        rows = len(matrix)
        cols = len(matrix[0])
        points = []

        # flood from ocean
        pacific_queue = []
        pacific_visited = [[0 for _ in range(cols)] for _ in range(rows)]
        atlantic_queue = []
        atlantic_visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            pacific_queue.append([i, 0])
            pacific_visited[i][0] = 1
        for i in range(cols):
            pacific_queue.append([0, i])
            pacific_visited[0][i] = 1

        for i in range(rows):
            atlantic_queue.append([i, cols-1])
            atlantic_visited[i][cols-1] = 1
        for i in range(cols):
            atlantic_queue.append([rows-1, i])
            atlantic_visited[rows-1][i] = 1

        p_visited = self.bfs_from_ocean(matrix, pacific_queue, pacific_visited)
        a_visited = self.bfs_from_ocean(matrix, atlantic_queue, atlantic_visited)

        for i in range(rows):
            for j in range(cols):
                if p_visited[i][j] == 1 and a_visited[i][j] == 1:
                    points.append([i, j])
        return points

    ###################################################################################################################
    ###################################################################################################################
    ############################################ NUM ISLANDS 200 ######################################################
    ###################################################################################################################
    ###################################################################################################################
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

if __name__ == "__main__":
    ###################################################################################################################
    ###################################################################################################################
    ############################################ DEEP COPY GRAPH 133 ##################################################
    ###################################################################################################################
    ###################################################################################################################
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n3, n1]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n3, n1]

    s = Solution()
    print(s.clone_graph_133(n1))
    print(s.clone_graph_133_DFS(n1))

    ###################################################################################################################
    ###################################################################################################################
    ############################################ COURSE SCHEDULE 207 ##################################################
    ###################################################################################################################
    ###################################################################################################################

    print(s.canFinish(2, [[1,0]])) # true
    print(s.canFinish(2, [[1,0],[0,1]])) # false

    ###################################################################################################################
    ###################################################################################################################
    ############################################ PACIFIC ATLANTIC WATER FLOW 417 ######################################
    ###################################################################################################################
    ###################################################################################################################
    print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
    # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]] in any order
    print(s.pacificAtlantic([]))
    # []

    ###################################################################################################################
    ###################################################################################################################
    ############################################ NUM ISLANDS 200 ######################################################
    ###################################################################################################################
    ###################################################################################################################