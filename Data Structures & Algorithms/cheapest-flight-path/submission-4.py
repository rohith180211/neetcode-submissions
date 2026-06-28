class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        ls=[[] for _ in range(n)]
        for start,end,price in flights:
            ls[start].append((price,end,1))
        heap=[]
        dist=[[sys.maxsize]*(k+2) for _ in range(n)]
        dist[src][0]=0
        heapq.heappush(heap,(0,src,0))
        while heap:
            cPrice,cNode,cStops=heapq.heappop(heap)
            if cNode==dst: return cPrice
            if cStops>k: continue
            
            for nPrice,nNode,nStops in ls[cNode]:
                if dist[nNode][cStops+1]>nPrice+cPrice:
                    dist[nNode][cStops+1]=nPrice+cPrice
                    heapq.heappush(heap,(nPrice+cPrice,nNode,cStops+1))
        return -1
