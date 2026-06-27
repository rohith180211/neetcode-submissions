class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ls=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for to,fro in prerequisites:
            ls[to].append(fro)
            indegree[fro]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res=0
        while q:
            curr=q.popleft()
            res+=1
            for neigh in ls[curr]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if res==numCourses:return True
        return False