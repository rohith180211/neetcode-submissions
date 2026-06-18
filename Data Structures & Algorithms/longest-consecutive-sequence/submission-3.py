class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set()
        for num in nums:
            st.add(num)
        n=len(nums)
        res=0
        for num in nums:
            if num-1 not in st:
                length=1
                while num+length in st:
                    length+=1
                res=max(length,res)
        return res
