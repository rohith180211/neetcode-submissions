class Solution:
    def isCycle(self,i:int,n:int,vis:List[int],ls:List[List[int]],parent:int)->bool:
        vis[i]=1
        for neigh in ls[i]:
            if vis[neigh]==0:
                if self.isCycle(neigh,n,vis,ls,i)==True:return True
            elif parent!=neigh:return True
        return False
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ls=[[] for _ in range(n)]
        for first,second in edges:
            ls[first].append(second)
            ls[second].append(first)
        vis=[0]*n
        if self.isCycle(0,n,vis,ls,-1)==True: return False
        for i in range(n):
            if vis[i]==0: return False
        
        return True
