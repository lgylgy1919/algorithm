def search1(nums, target):
    def binary_search(left, right):
        if left <= right:
            mid = (left_right) // 2

            if nums[mid] < target:
                return binary_search(mid + 1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid
        else:
            return -1

    return binary_search(0, len(nums) - 1)


def search2(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1


def search3(nums, target):
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index

    else:
        return -1


def search4(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1
