class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        for src,dest in tickets:
            heapq.heappush(graph[src],dest)
        res=[]
        def dfs(src):
            while graph[src]:
                nextStop=heapq.heappop(graph[src])
                dfs(nextStop)
            res.append(src)
        dfs("JFK")
        return res[::-1]