class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)

        adj_lst = [[] for _ in range(V)]
        for node in range(V):
            for adjNode in graph[node]:
                adj_lst[adjNode].append(node)
        
        indegrees = [0]*V

        for node in range(V):
            for adjNode in adj_lst[node]:
                indegrees[adjNode] += 1
        
        queue = deque()
        result = []
        for i in range(V):
            if indegrees[i] == 0 :
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for adjNode in adj_lst[curr]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] == 0 :
                    queue.append(adjNode)
        result.sort()
        return result
