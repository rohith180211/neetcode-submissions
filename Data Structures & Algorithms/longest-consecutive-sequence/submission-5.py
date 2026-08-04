class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res=0
        st=set()
        for num in nums:
            st.add(num)
        for num in nums:
            if num-1 not in st:
                length=1
                while num+length in st:
                    length+=1
                res=max(res,length)
        return res
