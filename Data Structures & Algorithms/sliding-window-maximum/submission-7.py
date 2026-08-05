class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        res=[]
        heap=[]
        for i in range(k):
            heapq.heappush(heap,(-nums[i],i))
        res.append(-heap[0][0])
        for right in range(k,n):
            left=right-k+1
            heapq.heappush(heap,(-nums[right],right))
            while heap[0][1]<left:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res
        

        