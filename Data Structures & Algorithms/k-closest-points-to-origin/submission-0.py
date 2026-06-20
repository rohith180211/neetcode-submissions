class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for point in points:
            x1=point[0]
            y1=point[1]
            dist=math.sqrt(x1*x1+y1*y1)
            heapq.heappush(heap,(-dist,point))
            if len(heap)>k:
                heapq.heappop(heap)
        res=[]
        for dist,point in heap:
            res.append(point)
        return res