import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet=set(wordList)
        if endWord not in wordSet: return 0
        q=deque()
        q.append((beginWord,1))
        if beginWord in wordSet:
            wordSet.remove(beginWord)
        while q:
            cWord,cNum=q.popleft()
            if cWord==endWord:return cNum
            charArray=list(cWord)

            for i in range(len(charArray)):
                ch=charArray[i]
                for letter in string.ascii_lowercase:
                    charArray[i]=letter
                    newStr="".join(charArray)
                    if newStr in wordList:
                        wordList.remove(newStr)
                        q.append((newStr,cNum+1))
                charArray[i]=ch
        return 0