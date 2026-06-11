class Node:
    def __init__(self):
        self.links=[None]*26
        self.flag=False
    def set_end(self)->None:
        self.flag=True
    def get(self,ch:str)->"Node":
        return self.links[ord(ch)-ord('a')]
    def put(self,ch:str,node:"Node")->None:
        self.links[ord(ch)-ord('a')]=node
    def containsKey(self,ch:str)->bool:
        return self.links[ord(ch)-ord('a')] is not None
    def is_end(self)->bool:
        return self.flag

class WordDictionary:

    def __init__(self):
        self.root=Node()

    def addWord(self, word: str) -> None:
        node=self.root
        for ch in word:
            if not node.containsKey(ch):
                node.put(ch,Node())
            node=node.get(ch)
        node.set_end()
    def search(self, word: str) -> bool:

        def dfs(index: int, node: Node) -> bool:
            if index == len(word):
                return node.is_end()

            ch = word[index]

            if ch == '.':
                for child in node.links:
                    if child is not None and dfs(index + 1, child):
                        return True
                return False

            else:
                if not node.containsKey(ch):
                    return False
                return dfs(index + 1, node.get(ch))

        return dfs(0, self.root)
        
