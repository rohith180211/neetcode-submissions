class Node:
    def __init__(self):
        self.links=[None]*26
        self.flag=False
    def set_end(self)->None:
        self.flag=True
    def contains_key(self,ch:str)->bool:
        return self.links[ord(ch)-ord('a')] is not None
    def put(self,ch:str,node:"Node")->None:
        self.links[ord(ch)-ord('a')]=node
    def is_end(self) -> bool:
        return self.flag
    def get(self, ch: str) -> "Node":
        return self.links[ord(ch) - ord('a')]

class PrefixTree:

    def __init__(self):
        self.root=Node()
    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch,Node())
            node=node.get(ch)
        node.set_end()

    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if not node.contains_key(ch):
                return False
            node=node.get(ch)
        return node.is_end()

    def startsWith(self, prefix: str) -> bool:
        node=self.root
        for ch in prefix:
            if not node.contains_key(ch):
                return False
            node=node.get(ch)
        return True
        