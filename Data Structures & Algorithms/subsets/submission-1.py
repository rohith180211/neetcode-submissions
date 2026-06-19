class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        subs=[]
        def backtrack(ind):
            if ind==n:
                res.append(subs.copy())
                return
            subs.append(nums[ind])
            backtrack(ind+1)
            subs.pop()
            backtrack(ind+1)
        backtrack(0)
        return res