"""

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_linked_list(arr):
    head = ListNode(arr[0])
    curr = head

    for i in range(1, len(arr)):
        num = arr[i]
        curr.next = ListNode(num)
        curr = curr.next

    return head

def print_linked_list(head):
    s = ""
    curr = head

    while curr:
        # print(s)
        s += f"{curr.val}"
        if curr.next:
            s += '->'
        curr = curr.next

    print(s)


# test_list = construct_linked_list([1,2,3,4,5])
# print_linked_list(test_list)


def partition(head, x):
    dummy = ListNode(0, head)
    curr = head
    less_prev = dummy
    greater_head = None
    greater_prev = None

    while curr:
        if curr.val >= x:
            if greater_head == None:
                greater_head = curr
            if greater_prev:
                greater_prev.next = curr
            greater_prev = curr
        else:
            less_prev.next = curr
            less_prev = curr
        curr = curr.next
    
    less_prev.next = greater_head
    greater_prev.next = None
    return dummy.next

test1 = construct_linked_list([1,4,3,2,5,2])
test_result1 = construct_linked_list([1,2,2,4,3,5])

test2 = construct_linked_list([2,1])
test_result2 = construct_linked_list([1,2])

result1 = partition(test1, 3)
print_linked_list(result1)

result2 = partition(test2, 2)
print_linked_list(result2)