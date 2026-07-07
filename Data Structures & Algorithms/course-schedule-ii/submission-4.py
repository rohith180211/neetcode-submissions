class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for second,first in prerequisites:
            graph[first].append(second)
            indegree[second]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res=[]
        while q:
            curr=q.popleft()
            res.append(curr)
            for neigh in graph[curr]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if len(res)==numCourses: return res
        return []