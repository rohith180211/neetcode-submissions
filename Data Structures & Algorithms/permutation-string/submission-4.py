class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1): return False
        arr1=[0]*26
        arr2=[0]*26
        for i in range (0,len(s1)):
            ind1=ord(s1[i])-ord('a')
            ind2=ord(s2[i])-ord('a')
            arr1[ind1]+=1
            arr2[ind2]+=1
        right=i
        left=0
        while right<len(s2):
            if arr1==arr2:
                return True
            right+=1
            if(right<len(s2)):
                arr2[ord(s2[right])-ord('a')]+=1
            arr2[ord(s2[left])-ord('a')]-=1
            left+=1
        return False