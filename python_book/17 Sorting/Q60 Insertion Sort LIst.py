def insertionSortList(head):
    # 초깃값 변경
    cur = parent = ListNode(0)
    while head:
        while cur.next and cur.next.val < head.val:
            cur = cur.next

        cur.next, head.next, head = head, cur.next, head.next

        # 필요한 경우에만 cur포인터가 되돌아가도록 처리
        if head and cur.val > head.val:
            cur = parent

    return parent.next