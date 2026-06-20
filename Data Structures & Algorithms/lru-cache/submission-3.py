class Node:
    def __init__(self,key,val):
        next=None
        prev=None
        self.key=key
        self.val=val
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=Node
        self.mp={}

    def get(self, key: int) -> int:
        if key not in self.mp: return -1
        node=self.mp[key]
        self.deleteNode(node)
        self.insertAfterHead(node)
        return node.val

    def deleteNode(self,node:Node)->None:
        prevNode=node.prev
        nextNode=node.next
        prevNode.next=nextNode
        nextNode.prev=prevNode
    def insertAfterHead(self,node:Node)->None:
        nodeCurrAfterHead=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=nodeCurrAfterHead
        nodeCurrAfterHead.prev=node
        

    def put(self, key: int, value: int) -> None:
        if key in self.mp:
            node=self.mp[key]
            node.val=value
            self.deleteNode(node)
            self.insertAfterHead(node)
        else:
            if self.capacity==len(self.mp):
                nodeToDelete=self.tail.prev
                self.deleteNode(nodeToDelete)
                del self.mp[nodeToDelete.key]
            newNode=Node(key,value)
            self.mp[key]=newNode
            self.insertAfterHead(newNode)
