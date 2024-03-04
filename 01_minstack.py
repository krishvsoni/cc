class Stack:
    def __init__(self):
        self.max = 100
        self.array = []
        self.top = -1

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFull(self):
        if self.top == self.max - 1:
            return True
        else:
            return False

    def push(self, data):
        if self.isFull():
            print("Stack overflow")
        else:
            self.top += 1
            self.array.append(data)
            print("Elements are:", self.array)

    def pop(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            a = self.array.pop()
            self.top -= 1
            print("Popped element is:", a)

    def minimum(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.min = self.array[0]
            for i in self.array:
                if self.min > i:
                    self.min = i
            print("Minimum element in stack is: ", self.min)

    def peek(self):
        if self.isEmpty():
            print("Stack underflow")
        else:
            print("Top element is:", self.array[self.top])

# Test the Stack class
if __name__ == "__main__":
    A = Stack()
    print("Is stack empty?", A.isEmpty())
    print("Is stack full?", A.isFull())
    A.push(10)
    A.push(20)
    A.push(30)
    A.push(40)
    A.pop()
    A.push(50)
    A.push(45)
    A.minimum()
    A.peek()
