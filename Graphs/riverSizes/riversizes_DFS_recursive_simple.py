def riversizes_dfs(matrix):
    rivers = []

    def appendRiver(i, j):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 1:
            matrix[i][j] += 1
            return 1 + appendRiver(i - 1, j) + appendRiver(i, j - 1) + appendRiver(i + 1, j) + appendRiver(i, j + 1)
        else:
            return 0

    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            river = appendRiver(i, j)
            if river > 0:
                rivers.append(river)

    return rivers
