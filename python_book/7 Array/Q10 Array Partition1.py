# Q10. 2n개의 인자를 가지고있는 array가 주어진다. n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
nums1 = [1, 2, 3, 4]
nums2 = [1, 2, 2, 5, 6, 6]

# 오름차순 풀이


def array_pair_sum(nums):
    sum = 0
    nums.sort()
    pair = []

    for n in nums:
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    print(sum)
    return sum


array_pair_sum(nums1)

# 짝수번째 합


def array_pair_sum2(nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    print(sum)
    return sum


array_pair_sum2(nums1)

# 슬라이싱 활용


def array_pair_sum3(nums):
    print(sum(sorted(nums)[::2]))
    return sum(sorted(nums)[::2])


array_pair_sum3(nums2)
