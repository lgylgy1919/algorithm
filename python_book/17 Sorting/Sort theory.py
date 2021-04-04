# 버블정렬
def bubblesort(A):
    for i in rangie(1, len(A)):
        for j in range(0, len(A - 1)):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]


# 퀵정렬
def quicksort(A, lo, hi):
    def partition(lo, hi):
        pivot = A[hi]
        left = lo
        for right in range(lo, hi):
            if A[right] < pivot:
                A[left], A[right] = A[right], A[left]
                left += 1
        A[left], A[hi] = A[hi], A[left]
        return left

    if lo < hi:
        pivot = partition(lo, hi)
        qucksort(A, lo, pivot - 1)
        quicksort(A, pivot + 1, hi)
