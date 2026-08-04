class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for word in strs:
            arr=[0]*26
            for ch in word:
                arr[ord(ch)-ord('a')]+=1
            arr=tuple(arr)
            if arr not in mp:
                mp[arr]=[]
            mp[arr].append(word)
        res=[]
        for value in mp.values():
            res.append(value)
        return res

                