from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges, source: int, destination: int) -> bool:
        # 1. DFS with recursion
        # 2. DFS with stack
        # 403. BFS with Dequeue
        if source == destination:
            return True

        # Adjacency list using dictionary
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = [False for _ in range(n)]
        seen[source] = True

        # 1
        # def dfs(i):
        #     if i == destination:
        #         return True
        #     for nei_node in graph[i]:
        #         if not seen[nei_node]:
        #             seen[nei_node] = True
        #             if dfs(nei_node):
        #                 return True
        #     return False
        # return dfs(source)

        # 2
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for nei_node in graph[node]:
                if not seen[nei_node]:
                    seen[nei_node] = True
                    stack.append(nei_node)
        return False
