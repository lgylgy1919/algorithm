# Q 배열을 받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 output array를 출력하라.
# 나눗셈을 활용하지 않고 Q(n)에 풀이하라.

nums = [1, 2, 3, 4]


def product_except_self(nums):
    output = []

    for i, n in enumerate(nums):
        j, k = 0, len(nums)-1
        elem = 1
        while j < i:
            elem *= nums[j]
            j += 1
        while k > i:
            elem *= nums[k]
            k -= 1

        output.append(elem)
    print(output)
    return output


# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
def product_except_self2(nums):
    out = []
    p = 1

    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p*nums[i]

    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, 0-1, -1):
        out[i] = out[i]*p
        p = p*nums[i]

    print(out)
    return out


product_except_self2(nums)
