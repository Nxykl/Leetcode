

def RemoveDuplicates(head):

    s = set()
    prev = None

    curr = head

    while curr != None:

        if curr.data in s:
            prev.next = curr.next
        else:
            s.add(curr.data)
            prev = curr
        curr = prev.next



    return head



