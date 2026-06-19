class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        res=[]
        currSub=[]
        def backtrack(ind,remaining):
            if remaining==0:
                res.append(currSub.copy())
                return
            if ind>=n or remaining<0:return
            currSub.append(nums[ind])
            backtrack(ind,remaining-nums[ind])
            currSub.pop()
            backtrack(ind+1,remaining)
        backtrack(0,target)
        return res