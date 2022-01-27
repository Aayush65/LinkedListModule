# This class is used to declare a Linked List
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

# This function converts the passed list into a linked list and returns the head of the Linked List
def listToLink(l : list) -> ListNode:
    dummy = curr = ListNode()
    for i in l:
        curr.next = ListNode(i)
        curr = curr.next
    return dummy.next

# This function converts all the nodes from the linked list passed as a head in this function, into list
def linkToList(head: ListNode) -> list:
    l = []
    while head:
        l.append(head.val)
        head = head.next
    return l

# This funtion returns the length of the linked list
def length(head: ListNode) -> int:
    n = 0
    while head:
        head = head.next
        n += 1
    return n

# This function appends the value passed into the function into the linked list and returns the resulting head
def append(head: ListNode, val: int) -> ListNode:
    dummy = curr = ListNode(None, head)
    while curr.next:
        curr = curr.next
    curr.next = ListNode(val)
    return dummy.next

# This function inserts the passed value at the provided index into the Linked List and returns the resultant head
def insert(head: ListNode, val: int, index: int) -> ListNode:
    dummy = curr = ListNode(None, head)
    while index > 0:
        curr = curr.next
        index -= 1
    curr.next = ListNode(val, curr.next)
    return dummy.next

# This function deletes the tail node and return the resulting head node
def pop(head: ListNode) -> ListNode:
    if not head: return
    dummy = curr = ListNode(None, head)
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return dummy.next

# This function deletes the node at the given index and returns the resulting head node
def delete(head: ListNode, index: int) -> ListNode:
    if not head: return
    dummy = curr = ListNode(None, head)
    while index > 0:
        curr = curr.next
        index -= 1
    curr.next = curr.next.next
    return dummy.next

# This function remove the number of instances (count) of an integer in the Linked List and returns the resulting head node
def remove(head: ListNode, val: int, count = 1) -> ListNode:
    # if count <= 0, then remove all
    dummy = curr = ListNode(None, head)
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
            count -= 1
            if count == 0: break
        else:
            curr = curr.next
    return dummy.next

# This function finds the first instance of an element in the Linked List and returns the index
def find(head: ListNode, val: int) -> int:
    curr = head
    index = -1
    while curr:
        if index < 0: index = 0
        if curr.val == val:
            return index
        curr = curr.next
        index += 1
    return index

# This function counts and returns the number of instances of the given integer in the Linked List 
def count(head: ListNode, val: int) -> int:
    curr = head
    n = 0
    while curr:
        if curr.val == val:
            n += 1
        curr = curr.next
    return n

# This function reverses the linked list and returns the new head node i.e. the tail node of the given Linked list
def reverse(head: ListNode) -> ListNode:
    left = None
    curr = head
    while curr: 
        right = curr.next
        curr.next = left
        left = curr
        curr = right
    return left

# This function prints out the linked list by using the passed head node
def printll(head: ListNode) -> None:
    curr = head
    while curr:
        print(curr.val, end = ' -> ')
        curr = curr.next
    print("None")

if __name__ == "__main__":
    # system("cls")
    a = listToLink([1,2,2,2,2,3,4,5,7])
    b = listToLink([1])
    c = listToLink([])