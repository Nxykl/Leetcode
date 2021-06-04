def reorder_list(head):
    fast,slow,prev = head,head,None

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        prev = slow
        print(fast.data, " ", slow.data," ", prev.data)
