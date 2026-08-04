class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        arr1=[0]*26
        arr2=[0]*26
        for i in range(len(s)):
            arr1[ord(s[i])-ord('a')]+=1
            arr2[ord(t[i])-ord('a')]+=1
        return arr1==arr2