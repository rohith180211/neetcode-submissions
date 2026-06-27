import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st=set(wordList)
        if endWord not in st:
            return 0
        q=deque()
        q.append((beginWord,1))
        if beginWord in st: st.remove(beginWord)
        while q:
            currWord,cSteps = q.popleft()
            if currWord==endWord:
                return cSteps
            charArray=list(currWord)
            for i in range(len(charArray)):
                curr=charArray[i]
                for letter in string.ascii_lowercase:
                    charArray[i]=letter
                    newStr="".join(charArray)
                    if newStr in st:
                        st.remove(newStr)
                        q.append((newStr,cSteps+1))
                charArray[i]=curr
        return 0
