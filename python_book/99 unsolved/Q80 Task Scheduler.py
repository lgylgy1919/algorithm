import collections

tasks1 = ["A", "A", "A", "B", "B", "B"]
n1 = 2
# output = 8 (A->B->IDLE->A->B->IDLE->A->B)

tasks2 = ["A", "A", "A", "B", "C", "D"]
n2 = 2
# output = 7 (A->B->IDLE->A->C->D->A)


def leastInterval(tasks, n):
    counter = collections.Counter(tasks)
    result = 0

    while True:
        sub_count = 0
        # 개수 순 추출
        for task, _ in counter.most_common(n + 1):
            sub_count += 1
            result += 1

            counter.subtract(task)
            # 0 이하인 아이템을 목록에서 완전히 제거
            counter += collections.Counter()

        if not counter:
            break

        result += n - sub_count + 1

    print(result)
    return result


leastInterval(tasks1, n1)