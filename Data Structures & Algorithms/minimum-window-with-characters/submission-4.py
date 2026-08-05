class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp=defaultdict(int)
        minLen=sys.maxsize
        sIndex=-1
        for i in range(len(t)):
            mp[t[i]]+=1
        count=0
        i=0
        for j in range(len(s)):
            mp[s[j]]-=1
            if mp[s[j]]>=0:
                count+=1
            while count==len(t):
                if j-i+1<minLen:
                    minLen=j-i+1
                    sIndex=i
                mp[s[i]]+=1
                if mp[s[i]]>0:
                    count-=1
                i+=1
        if minLen==sys.maxsize: return ""
        return s[sIndex:sIndex+minLen]