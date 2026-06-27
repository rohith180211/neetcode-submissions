class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ls=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        for to,fro in prerequisites:
            ls[fro].append(to)
            indegree[to]+=1
        q=deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
        res=[-1]*numCourses
        i=0
        while q:
            curr=q.popleft()
            res[i]=curr
            i+=1
            for neigh in ls[curr]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if i==numCourses:return res
        return []