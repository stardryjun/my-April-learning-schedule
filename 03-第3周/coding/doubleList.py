class DoubleListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None
    def print(self):
        temp = self
        while temp:
            print(temp.val,end=' ')
            temp = temp.next

def insert(head, val, index):
    if index < 0:
        print('index out of range')
        return head
    newNode = DoubleListNode(val)
    if index == 0:
        head.prev = newNode
        newNode.next = head
        head = newNode
        return head
    temp = head
    for i in range(index-1):
        temp = temp.next
    if temp.next:
        temp.next.prev = newNode
        newNode.next = temp.next
    temp.next = newNode
    newNode.prev = temp
    return head

def delete(head, index):
    if index < 0:
        print('index out of range')
        return head
    if index == 0:
        head = head.next
        head.prev = None
        return head
    temp = head
    for i in range(index-1):
        if not temp.next:
            print('index out of range')
            return head
        temp = temp.next
    if temp.next:
        temp.next = temp.next.next
        if temp.next.next:
            temp.next.prev = temp
    return head

doubleList = DoubleListNode(0)
doubleList = insert(doubleList,1,0)
doubleList = insert(doubleList,2,1)
doubleList = insert(doubleList,3,2)
doubleList.print()
print()
doubleList = delete(doubleList,2)
doubleList = delete(doubleList,0)
doubleList.print()
