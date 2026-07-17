class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        LPS=""
        for i in range(n):
            #odd length palindrome
            low=i
            high=i
            while low>=0 and high<n and s[low]==s[high]:
                subsString=s[low:high+1]
                if len(subsString)>len(LPS):
                    LPS=subsString
                low-=1
                high+=1
            #even length
            low=i
            high=i+1
            while low>=0 and high<n and s[low]==s[high]:
                subsString=s[low:high+1]
                if len(subsString)>len(LPS):
                    LPS=subsString
                low-=1
                high+=1
        return LPS
