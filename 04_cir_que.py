class Queue:
    def __init__(self, K):
        self.size = 0
        self.capacity = K
        self.array = [None] * K
        self.front = self.rear = -1

    def isempty(self):
        return self.size == 0

    def isfull(self):
        return self.size == self.capacity

    def enqueue(self, data):
        if self.isfull():
            print("Queue is full")
            return
        if self.isempty(): 
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity 
        self.array[self.rear] = data
        self.size += 1
        print("Element enqueued:", self.array[self.rear])

    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
            return None
        value = self.array[self.front]
        if self.front == self.rear:
            self.rear = self.front = -1
        else:
            self.front = (self.front + 1) % self.capacity 
        self.size -= 1
        print("Deleted element is:", value)
        return value

    def fElement(self):
        if self.isempty():
            print("Queue is empty")
            return None
        return self.array[self.front]

    def rElement(self):
        if self.isempty():
            print("Queue is empty")
            return None
        return self.array[self.rear]
    
# size=10 
# q=queue(size) 
# q.enqueue(10) 
# q.enqueue(20) 
# q.enqueue(30) 
# q.enqueue(40) 
# q.dequeue() 
# q.enqueue(50) 
# q.enqueue(60) 
# q.dequeue()
# print("front element",q.fElement()) 
# print("rear element",q.rElement())