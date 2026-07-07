class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph=[[] for _ in range(n)]
        for u,v,price in flights:
            graph[u].append((price,v))
        heap=[]
        heapq.heappush(heap,(0,src,0))
        dist=[[sys.maxsize]*(k+2) for _ in range(n)]
        dist[src][0]=0
        while heap:
            cPrice,cFlight,cStops=heapq.heappop(heap)
            
            if cFlight==dst:return cPrice
            if cStops>k:continue
            for newPrice,newNode in graph[cFlight]:
                if newPrice+cPrice<dist[newNode][cStops+1]:
                    dist[newNode][cStops+1]=newPrice+cPrice
                    heapq.heappush(heap,(newPrice+cPrice,newNode,cStops+1))
        return -1