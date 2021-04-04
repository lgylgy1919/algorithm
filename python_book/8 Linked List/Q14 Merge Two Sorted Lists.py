l1 = [1, 2, 4]
l2 = [1, 3, 4]


def merge_two_lists1(l1, l2):
    answer = []
    for i in range(0, len(l1) + len(l2)):
        if l1 and l2:
            if l1[0] <= l2[0]:
                answer.append(l1.pop(0))
            else:
                answer.append(l2.pop(0))
        elif l1:
            answer.append(l1.pop(0))
        elif l2:
            answer.append(l2.pop(0))
    print(answer)
    return answer


merge_two_lists1(l1, l2)


# solution
def mergeTwoLists(self, l1, l2):
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next, l2)
    return l1
