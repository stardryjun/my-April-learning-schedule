class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def insert(self, index, val):
        if index == 0:
            new_node = ListNode(val)
            new_node.next = self
            return new_node
        current = self
        for _ in range(index - 1):
            if current.next is None:
                break
            current = current.next
        new_node = ListNode(val)
        new_node.next = current.next
        current.next = new_node
        return self
    def delete(self, index):
        if index == 0:
            return self.next
        current = self
        for _ in range(index - 1):
            if current.next is None:
                return self
            current = current.next
        if current.next is not None:
            current.next = current.next.next
        return self
    def __str__(self):
        values = []
        current = self
        while current is not None:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)

list1 = ListNode(1)
list1.insert(1, 2)
list1.insert(2, 3)
print(list1)  # 输出: 1 -> 2 -> 3
list1.delete(1)
print(list1)  # 输出: 1 -> 3
