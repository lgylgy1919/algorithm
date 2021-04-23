import collections


def majorityElement1(nums):
    for num in nums:
        if nums.count(num) > len(nums) // 2:
            return num


def majorityElement2(nums):
    counts = collections.defaultdict(int)
    for num in nums:
        if counts[num] == 0:
            counts[num] = nums.count(num)

        if counts[num] > len(nums) // 2:
            print(num)
            return num


def majorityElement3(nums):
    if not nums:
        return None
    if len(nums) == 1:
        return nums[0]

    half = len(nums) // 2
    a = self.majorityElement3(nums[:half])
    b = self.majorityElement3(nums[half:])

    return [b, a][nums.count(a) > half]


def majorityElement4(nums):
    return sorted(nums)[len(nums) // 2]


nums = [2, 2, 1, 1, 1, 2, 2]
majorityElement2(nums)