def riversizes_dfs_optimized(matrix):
    rivers = []
    stack = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                length = 0
                first = (i, j)
                stack.append(first)
                while len(stack) > 0:
                    length += matrix[i][j]
                    matrix[i][j] = 0
                    # Go up
                    if i - 1 > -1 and matrix[i - 1][j] == 1:
                        stack.append((i, j))
                        i = i - 1
                    # Go left
                    elif j - 1 > -1 and matrix[i][j - 1] == 1:
                        stack.append((i, j))
                        j = j - 1
                    # Go down
                    elif i + 1 < len(matrix) and matrix[i + 1][j] == 1:
                        stack.append((i, j))
                        i = i + 1
                    # Go right
                    elif j + 1 < len(matrix[0]) and matrix[i][j + 1] == 1:
                        stack.append((i, j))
                        j = j + 1
                    else:
                        i, j = stack.pop()
                else:
                    rivers.append(length)
    return rivers
