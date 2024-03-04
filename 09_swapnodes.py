class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 

    def Swap(self):
        temp = self.head 
        if temp is None:
            return
        while temp and temp.next: 
            if temp.data != temp.next.data:
                temp.data, temp.next.data = temp.next.data, temp.data 
            temp = temp.next.next

    def push(self, data): 
        new_node = Node(data) 
        new_node.next = self.head 
        self.head = new_node

    def printlist(self): 
        temp = self.head
        while temp: 
            print(temp.data, end="-->") 
            temp = temp.next 
        print("None")

# Example usage:
if __name__ == "__main__":
    l = LinkedList() 
    l.push(1)
    l.push(2)
    l.push(3)
    l.push(4)
    print("Linked list without swap:") 
    l.printlist()
    l.Swap()
    print("List after swap:") 
    l.printlist()
