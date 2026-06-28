class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ls=[[] for _ in range(n+1)]
        for u,v,t in times:
            ls[u].append((t,v))
        heap=[]
        heapq.heappush(heap,(0,k))
        dist=[sys.maxsize]*(n+1)
        dist[k]=0
        time=0
        while heap:
            cTime,node =heapq.heappop(heap)
            if dist[node]<cTime:continue
            for nTime,nNode in ls[node]:
                if nTime+cTime<dist[nNode]:
                    dist[nNode]=nTime+cTime
                    heapq.heappush(heap,(nTime+cTime,nNode))
        for i in range(1,n+1):
            if dist[i]==sys.maxsize:return -1
            time=max(time,dist[i])
        return time
