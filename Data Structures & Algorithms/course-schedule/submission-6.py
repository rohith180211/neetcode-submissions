class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ls=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for a,b in prerequisites:
            ls[b].append(a)
            indegree[a]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        size=0
        while q:
            curr=q.popleft()
            size+=1
            for neigh in ls[curr]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if size==numCourses: return True
        return False
