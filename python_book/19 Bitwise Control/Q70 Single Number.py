def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
        print(result)
    return result


nums = [4, 1, 2, 1, 2]
singleNumber(nums)
