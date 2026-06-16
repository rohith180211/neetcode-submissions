import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ls=[[] for _ in range(n+1)]
        for u,v,t in times:
            ls[u].append((t,v))
        dist=[sys.maxsize]*(n+1)
        dist[k]=0
        heap=[]
        heapq.heappush(heap,(0,k))
        while heap:
            cTime,cNode=heapq.heappop(heap)
            if cTime>dist[cNode]: continue
            for nTime,nNode in ls[cNode]:
                if dist[nNode]>nTime+cTime:
                    dist[nNode]=nTime+cTime
                    heapq.heappush(heap,(dist[nNode],nNode))
        res=0
        for i in range(1,n+1):
            if dist[i]==sys.maxsize:return -1
            res=max(res,dist[i])
        return res