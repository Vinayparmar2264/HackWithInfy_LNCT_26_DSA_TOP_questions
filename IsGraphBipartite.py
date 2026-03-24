class Solution:
    def dfs(self,curr_node,visited,graph,color):
        visited[curr_node]  = color
        for adjNode in graph[curr_node]:
            if visited[adjNode] == -1 :
                ans = self.dfs(adjNode,visited,graph,1-color)
                if ans == False:
                    return False

            else:
                if visited[curr_node] == visited[adjNode]:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        size = len(graph)
        visited = [-1]*size

        for i in range(size):
            if visited[i] != -1:
                continue
            elif visited[i] == -1:
                ans = self.dfs(i,visited,graph,0)
                if ans == False:
                    return False
        return True
