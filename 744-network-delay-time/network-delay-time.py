class Solution:
    class Edge:
        def __init__(self, node, wt):
            self.node = node
            self.wt = wt
            
    def dijkstra(self, V: int, edges: list[list[int]], s: int) -> list[int]:
        # code here
        graph = [[] for _ in range(V)]
        
        for e in edges:
            src = e[0]
            dst = e[1]
            wt = e[2]
            
            graph[src].append(self.Edge(dst, wt))
            # graph[dst].append(self.Edge(src, wt))
            
        dist = [float('inf')] * V
        
        dist[s] = 0
        
        pq = []
        
        heapq.heappush(pq, (0, s))
        
        while pq:
            cost, node = heapq.heappop(pq)
            
            if dist[node] < cost:
                continue
            
            for edge in graph[node]:
                nbrVtx = edge.node
                travelCost = edge.wt
                
                if dist[node] + travelCost < dist[nbrVtx]:
                    dist[nbrVtx] = dist[node] + travelCost
                    heapq.heappush(pq, (dist[node] + travelCost, nbrVtx))
                    
        return dist
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dist = self.dijkstra(n+1, times, k)

        ans = 0
        for i in range(1, n+1):
            if dist[i] == float('inf'):
                return -1
            ans = max(ans, dist[i])
            
        return ans