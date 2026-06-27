class Solution:
    def bfs(self,i:int,vis:List[int],ls:List[List[int]],n:int)->None:
        vis[i]=1
        q=deque()
        q.append(i)
        while q:
            curr=q.popleft()
            for neigh in ls[curr]:
                if vis[neigh]==0:
                    vis[neigh]=1
                    q.append(neigh)
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ls=[[] for _ in range(n)]
        for first,second in edges:
            ls[first].append(second)
            ls[second].append(first)
        vis=[0]*n
        count=0
        for i in range(n):
            if vis[i]==0:
                count+=1
                self.bfs(i,vis,ls,n)
        return count
