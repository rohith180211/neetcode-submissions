class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        n=len(nums)
        prefix=0
        suffix=0
        for i in range(len(nums)):
            prefix=nums[i]*1 if prefix ==0 else nums[i]*prefix
            suffix=nums[n-1-i]*1 if suffix ==0 else nums[n-1-i]*suffix
            res=max(res,max(prefix,suffix))
        return res

            