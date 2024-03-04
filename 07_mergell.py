class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode()
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return dummy.next

def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
if __name__ == "__main__":
    # Creating the first sorted linked list: 1 -> 3 -> 5
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    # Creating the second sorted linked list: 2 -> 4 -> 6
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    print("First sorted linked list:")
    printLinkedList(l1)

    print("\nSecond sorted linked list:")
    printLinkedList(l2)

    merged_list = mergeTwoLists(l1, l2)
    print("\nMerged sorted linked list:")
    printLinkedList(merged_list)
