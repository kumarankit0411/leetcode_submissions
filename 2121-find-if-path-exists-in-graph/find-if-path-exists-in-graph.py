class Solution:
    def bfs(self, adj, src, dest):
        vis = [False] * len(adj)
        
        q = deque()
        q.append(src)
        
        ans = []
        
        while len(q) > 0:
            fnt = q.popleft()
            if fnt == dest:
                return True
            
            if vis[fnt] == True:
                continue
            vis[fnt] = True
            ans.append(fnt)
            
            for nbr in adj[fnt]:
                if vis[nbr] == False:
                    q.append(nbr)
                    
        return False
    
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return self.bfs(adj, source, destination)