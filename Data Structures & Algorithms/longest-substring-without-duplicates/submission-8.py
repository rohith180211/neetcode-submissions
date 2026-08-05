class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        left=0
        n=len(s)
        res=0
        for right in range(n):
            while s[right] in st:
                st.remove(s[left])
                left+=1
            st.add(s[right])
            res=max(res,right-left+1)
        return res