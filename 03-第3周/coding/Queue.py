class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None
    
    def size(self):
        return len(self.items)
    
q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())  # Output: 1
print(q.peek())  # Output: 2
print(q.size())  # Output: 2