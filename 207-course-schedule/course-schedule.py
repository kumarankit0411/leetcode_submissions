class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        
        indegree = [0] * numCourses
        
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v]+=1
            
        q = deque()
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        ans = []    
        while q:
            node = q.popleft()
            
            ans.append(node)
            
            for nbr in graph[node]:
                indegree[nbr]-=1
                if indegree[nbr] == 0:
                    q.append(nbr)
                    
        if len(ans) == numCourses:
            return True
        else:
            return False