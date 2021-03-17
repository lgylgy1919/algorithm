"""
candidates = [2,3,6,7], target = 7
[ [7],[2,2,3]]

candidates = [2,3,5], target = 8
[[2,2,2,2], [2,3,3],[3,5]]
"""


def combinationSum():
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum < 0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신부터 하위 원소 까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum - candidates[i], i, path + [candidates[i]])

    dfs(target, 0, [])
    return result