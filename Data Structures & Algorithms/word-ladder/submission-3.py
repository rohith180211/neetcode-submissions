import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st=set()
        for word in wordList:
            st.add(word)
        if endWord not in st: return 0
        ls=[[] for _ in range(26)]
        q=deque()
        q.append((beginWord,1))
        st.discard(beginWord)
        while q:
            currWord,currSteps=q.popleft()
            if currWord==endWord: return currSteps
            charArray=list(currWord)
            for i in range(len(charArray)):
                original=charArray[i]
                for letter in string.ascii_lowercase:
                    if letter==original: continue
                    charArray[i]=letter
                    newWord="".join(charArray)
                    if newWord in st:
                        q.append((newWord,currSteps+1))
                        st.remove(newWord)
                charArray[i]=original
        return 0
