class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        mp={} #val-index
        for i in range(n):
            toFind=target-nums[i]
            if toFind in mp:return [mp.get(toFind),i]
            mp[nums[i]]=i
        return [-1,-1]