def searchMatrix(matix, target):
    # 예외 처리
    if not matrix:
        return False

    # 첫 행의  맨 뒤
    row = 0
    col = len(matix[0]) - 1

    while row <= len(matix) - 1 and col >= 0:
        if target == matrix[row][col]:
            return True
        # 타겟이 작으면 왼쪽으로 이동
        elif target < matrix[row][col]:
            col -= 1
        # 타겟이 크면 오른쪽으로 이동
        elif target > matrix[row][col]:
            row += 1

        return False


def searchMatrix(matrix, target):
    return any(target in row for row in matrix)