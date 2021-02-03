nums = [1, 8, 11, 15]
target = 9


# Brute-Force
def sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return[i, j]


# in 을 이용한 탐색
def sum_using_in(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i+1:]:
            print(nums.index(n), nums.index(complement))
            return nums.index(n), nums[i+1:].index(complement)+(i+1)


# 첫 번째 수를 뺀 결과 키 조회
def twoSum_3(nums, target):
    nums_map = {}
    # 키와 값을 바꿔 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
        # nums_map = {"2":0, "7":1, "11":2, "15":3}

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target-num]:
            print(nums.index(num), nums_map[target-num])
            return nums.index(num), nums_map[target-num]


#  and i != nums_map[target-num]
twoSum_3(nums, target)

# 조회 구조 개선


def twoSum_4(nums, target):
    nums_map = {}
    # 하나의 for문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i
