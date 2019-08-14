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
    ############################################ COURSE SCHEDULE 207 ##################################################
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