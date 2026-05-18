class heapify:
    def __init__(self, arr):
        self.arr = arr
        self.size = len(arr)

    def heapify(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.sift_down(i)

    def sift_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < self.size and self.arr[left] < self.arr[smallest]:
            smallest = left

        if right < self.size and self.arr[right] < self.arr[smallest]:
            smallest = right

        if smallest != index:
            self.arr[index], self.arr[smallest] = self.arr[smallest], self.arr[index]
            self.sift_down(smallest)
    
    def sift_down2(self, index):
        minchild = 2*index + 1
        while minchild < self.size:
            if minchild + 1 < self.size and self.arr[minchild + 1] < self.arr[minchild]:
                minchild += 1
            if self.arr[index] > self.arr[minchild]:
                self.arr[index], self.arr[minchild] = self.arr[minchild], self.arr[index]
                index = minchild
                minchild = 2*index + 1
            else:
                break