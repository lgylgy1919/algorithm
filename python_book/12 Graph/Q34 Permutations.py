"""
Example1)
Input : nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example2)
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example3)
Input: nums = [1]
Output: [[1]]

All the integers of nums are unique.
"""


def permutations(nums):

    output = []

    for i in nums:
        permu = []
        permu.append(i)
        output.append(permu)

    print(output)
    return output


nums = [1, 2, 3]
permutations(nums)