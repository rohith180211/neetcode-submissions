class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ls=[[] for _ in range(numCourses)]
        indegree=[0]*numCourses
        res=[-1]*numCourses
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
            res[size]=curr
            size+=1
            for neigh in ls[curr]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)
        if size==numCourses: return res
        return []