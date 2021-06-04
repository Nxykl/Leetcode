


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
def fn_print(head):
    while head != None:
        print(head.data, end=' ')
        head = head.next
def takeinput():
    head = None
    tail = None
    data = int(input())

    while data != -1:
        n = Node(data)

        if head == None:
            head = n
            tail = n
        else:
            tail.next = n
            tail = n

        data = int(input())
    return head
def length(head):
    count = 0
    while head != "Null":
        count = count + 1
        head = head.next

    return count
def print_ith_node(head, index):
    count = 0;
    if index < 0:
        return -1
    while count <= index and head != "Null":
        if count == index:
            return head.data
        else:
            head = head.next
        count = count + 1
def insert(head, index):
    data = 0
    count = 1
    if index == 0:
        data = int(input())
        n = Node(data)
        n.next = head
        return head

    copyhead = head

    while count <= index and head != "Null":
        head = head.next
        count = count + 1
    temp = head.next
    if head != "Null":
        data = int(input())
        n = Node(data)
        head.next = n
        n.next = temp
    return copyhead
def reverse_linked_list(head):
    curr = head
    prev = "Null"

    while curr != "Null":
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev
def reverse_pos(head, m, n):
    count = 1
    curr = head
    start = head

    while count < m:
        start = curr
        curr = curr.next
        count = count + 1

    new_list = None
    tail = curr

    while count >= m and count <= n:
        next_val = curr.next
        curr.next = new_list
        new_list = curr
        curr = next_val
        count = count + 1

    start.next = new_list
    tail.next = curr

    if m > 1:
        return head
    else:
        return new_list
    return head
def length_recursive(head, count):
    if head == None:
        return count
    else:
        head = head.next
        count = count + 1
        return length_recursive(head, count)
def is_present(head, data):
    while head != None:
        if head.data == data:
            return True
        head = head.next

    return False
def recursive_is_present(head, data):
    if head == None:
        return False
    if head.data == data:
        return True
    return recursive_is_present(head.next, data)

def remove_Node(head, n):
    # remove nth node from the end of the list
    # my Solution


    if head.next == None and n == 1:
        return None
    elif head == None:
        return head


    temp = head
    count = 0
    length = 0
    while temp != None:
        count = count+1
        temp = temp.next
    count = count - n
    temp_head = head
    while temp_head != None:
        curr = temp_head
        length = length +1
        temp_head = temp_head.next

        if count == length:
            next_val = temp_head.next
            curr.next = next_val

    return head


#head = takeinput()
#n = int(input())
#cp_head = remove_Node(head,n)
#fn_print(cp_head)
#

# m = int(input())
# n = int(input())
#data = int(input())

#print(recursive_is_present(head, data))

# cp_head = reverse_pos(head,m,n)
# fn_print(cp_head)