class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def findMergePoint(headA, headB):
    pointerA = headA
    pointerB = headB

    while pointerA != pointerB:
        if pointerA is None:
            pointerA = headB
        else:
            pointerA = pointerA.next
        
        if pointerB is None:
            pointerB = headA
        else:
            pointerB = pointerB.next

    return pointerA

# Example usage:
if __name__ == "__main__":
    # Creating the first sorted linked list: 1 -> 3 -> 5 -> 7 -> 9 -> None
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(5)
    list1.next.next.next = ListNode(7)
    list1.next.next.next.next = ListNode(9)

    # Creating the second sorted linked list: 2 -> 4 -> 7 -> 9 -> None
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list2.next.next = list1.next.next.next  # Merge point at node with value 7

    merge_point = findMergePoint(list1, list2)
    if merge_point:
        print("Merge point value:", merge_point.val)
    else:
        print("No merge point found")
