class Node:
    def __init__(self):
        self.links=[None]*26
        self.word=None
    def set_end(self,word:str)->None:
        self.word=word
    def contains_key(self,ch:str)->bool:
        return self.links[ord(ch)-ord('a')] is not None
    def put(self,ch:str,node:"Node")->None:
        self.links[ord(ch)-ord('a')]=node
    def get(self, ch: str) -> "Node":
        return self.links[ord(ch) - ord('a')]

class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch,Node())
            node=node.get(ch)
        node.set_end(word)
        
class Solution:
    dr=[-1,1,0,0]
    dc=[0,0,1,-1]
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie=Trie()
        for word in words:
            trie.insert(word)
        n=len(board)
        m=len(board[0])
        res=[]
        for i in range(n):
            for j in range(m):
                self.dfs(i,j,res,board,words,trie.root)
        return res
    def dfs(self,r:int,c:int,res:List[str], board: List[List[str]], words: List[str],node:"Node")->None:
        if r<0 or c<0 or r>=len(board) or c>=len(board[0]):return 
        ch=board[r][c]
        if ch=='#' or node.contains_key(ch)==False:
            return
        node=node.get(ch)
        if node.word!=None:
            res.append(node.word)
            node.word=None
        board[r][c]='#'
        for k in range(4):
            self.dfs(r+self.dr[k],c+self.dc[k],res,board,words,node)
        board[r][c]=ch