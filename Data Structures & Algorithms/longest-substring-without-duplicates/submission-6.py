class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        n=len(s)
        res=0
        i=0
        for j in range(n):
            while s[j] in st:
                st.remove(s[i])
                i+=1
            st.add(s[j])
            res=max(res,j-i+1)
        return res