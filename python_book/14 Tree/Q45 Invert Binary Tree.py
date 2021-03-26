def inverTree1(root):
    if root:
        root.left, root.right = self.invertTree1(root.right), self.invertTree1(
            root.left
        )
        return root
    return None


def invertTree2(root):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        # 부모 노드로부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

        return root


def inverTree3(root):
    stack = collections.deque([root])

    while stack:
        node = stack.pop()
        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)

        return root


def inverTree4(root):
    stack = collections.deque([root])

    while stack:
        node = stack.pop()

        if node:
            stack.append(node.left)
            stack.append(node.right)

            node.left, node.right = node.right, node.left  # 후위 순위

    return root