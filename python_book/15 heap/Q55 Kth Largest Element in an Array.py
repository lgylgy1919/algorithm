import heapq


def findKthLargest1(nums, k):
    heap = list()
    for n in nums:
        heapq.heappush(heap, -n)

    for _ in range(k):
        heapq.heappop(heap)

    print(-heapq.heappop(heap))
    return -heapq.heappop(heap)


def findKthLargest2(nums, k):
    heapq.heapify(nums)

    for _ in range(len(nums) - k):
        heapq.heappop(nums)

    print(heapq.heappop(nums))
    return heapq.heappop(nums)


def findKthLargest3(nums, k):
    print(heapq.nlargest(k, nums)[-1])
    return heapq.nlargest(k, nums)[-1]


def findKthLargest4(nums, k):
    print(sorted(nums, reverse=True)[k - 1])
    return sorted(nums, reverse=True)[k - 1]


nums1 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
nums3 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
nums4 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

findKthLargest1(nums1, k)
findKthLargest2(nums2, k)
findKthLargest3(nums3, k)
findKthLargest4(nums4, k)
