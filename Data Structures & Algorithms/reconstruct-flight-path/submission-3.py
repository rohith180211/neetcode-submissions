class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        res=[]
        for src,dest in tickets:
            heapq.heappush(graph[src],dest)
        def dfs(node):
            while graph[node]:
                nextStop=heapq.heappop(graph[node])
                dfs(nextStop)
            res.append(node)
        dfs("JFK")
        return res[::-1]