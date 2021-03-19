"""
Example1)
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Example2)
Input: n = 1, k = 1
Output: [[1]]



"""


def combine(n, k):
    results = []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])

        for i in range(start, n + 1):
            elements.append(i)
            print(elements, k)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)
    print(results)
    return results


combine(4, 2)
