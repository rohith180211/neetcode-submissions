class Solution:
    def compare(self,word1:str,word2:str,graph:List[Set()],indegree:List[int])->None:
        i=0
        j=0
        while i<len(word1) and j<len(word2):
            if word1[i]!=word2[j]:
                index1=ord(word1[i])-ord('a')
                index2=ord(word2[j])-ord('a')
                if index2 not in graph[index1]:
                    graph[index1].add(index2)
                    indegree[index2]+=1
                break
            i+=1
            j+=1
    def foreignDictionary(self, words: List[str]) -> str:
        n=len(words)
        indegree=[0]*26
        present=[0]*26
        for word in words:
            for ch in word:
                index=ord(ch)-ord('a')
                present[index]=1
        graph=[set() for _ in range(26)]
        for i in range(1,n):
            if len(words[i-1])>len(words[i]) and words[i-1].startswith(words[i]):return ""
            self.compare(words[i-1],words[i],graph,indegree)
        
        heap=[]
        for i in range(26):
            if indegree[i]==0 and present[i]==1:
                heapq.heappush(heap,chr(i+ord('a')))
        res=""
        while heap:
            ch=heapq.heappop(heap)
            res+=ch
            for neigh in graph[ord(ch)-ord('a')]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    heapq.heappush(heap,chr(neigh+ord('a')))
        countPresent=0
        for val in present:
            if val==1:countPresent+=1
        if len(res)==countPresent:return res
        return ""

