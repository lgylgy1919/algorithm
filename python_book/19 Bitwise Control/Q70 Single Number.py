def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    print(result)
    return result


nums = [2, 2, 1, 3, 1, 4, 3, 4, 1]
singleNumber(nums)
