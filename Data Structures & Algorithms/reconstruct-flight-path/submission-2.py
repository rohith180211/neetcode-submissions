class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res=[]
        graph=defaultdict(list)
        for src,dest in tickets:
            heapq.heappush(graph[src],dest)
        def backtrack(node):
            while graph[node]:
                nextStop=heapq.heappop(graph[node])
                backtrack(nextStop)
            res.append(node)
        backtrack("JFK")
        return res[::-1]
        