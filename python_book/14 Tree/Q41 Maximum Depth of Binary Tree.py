import collections


def maxDepth(root):
    if root is None:
        return 0
    queue = collections.deque([root])
    print(queue)
    depth = 0

    while queue:
        depth += 1
        # 큐 연산 추출 노드의 자식노드 삽입
        for _ in range(len(queue)):
            cur_root = queue.popleft()
            if cur_root.left:
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

        # BFS 반복횟수 == 깊이
        return depth


root = [3, 9, 20, None, None, 15, 7]
maxDepth(root)
