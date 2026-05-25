class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        
        self.head=None
        self.count=0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.count:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        return curr.val

    def addAtHead(self, val: int) -> None:
        newnode=Node(val)
        newnode.next=self.head
        self.head=newnode
        self.count+=1

    def addAtTail(self, val: int) -> None:
        newnode = Node(val)
        if not self.head:
            self.head = newnode
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = newnode
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.count:
            return   
        if index == 0:
            self.addAtHead(val)
            return
        
        current=self.head
        for _ in range(index-1):
            current=current.next
        newnode=Node(val)
        newnode.next=current.next
        current.next=newnode
        self.count+=1

    def deleteAtIndex(self, index: int) -> None:
        
        if index < 0 or index >= self.count:
            return
        
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            
            curr.next = curr.next.next
        
        self.count -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)