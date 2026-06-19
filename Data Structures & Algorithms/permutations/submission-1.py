class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        n=len(nums)
        used=[False]*n
        def backtrack():
            if len(subset)==n:
                res.append(subset.copy())
                return
            for ind in range(n):
                if used[ind]==False:
                    used[ind]=True
                    subset.append(nums[ind])
                    backtrack()
                    used[ind]=False
                    subset.pop()
        backtrack()
        return res