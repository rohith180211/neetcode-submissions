class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        mp={}
        for i in range(n):
            value=target-nums[i]
            if value in mp:return [mp[value],i]
            mp[nums[i]]=i
        return [-1,-1]