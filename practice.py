import collections

root = [3, 9, 20, None, None, 15, 7]
queue = collections.deque([root])
print(queue)
print(len(queue))
cur_root = queue.popleft()
print(cur_root)
