class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for second,first in prerequisites:
            graph[first].append(second)
            indegree[second]+=1
        
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        index=0
        while q:
            curr=q.popleft()
            index+=1
            for neigh in graph[curr]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if index==numCourses: return True
        return False
        
