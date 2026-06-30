class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        mp=defaultdict(int)
        maxFreq=0
        maxLen=0
        i=0
        for j in range(n):
            mp[s[j]]+=1
            maxFreq=max(maxFreq,mp[s[j]])
            while (j-i+1)-maxFreq>k:
                mp[s[i]]-=1
                if mp[s[i]]==0:
                    del mp[s[i]]
                i+=1
            maxLen=max(maxLen,j-i+1)
        return maxLen