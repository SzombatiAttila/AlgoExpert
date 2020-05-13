def riversizes_dfs(matrix):
    index = 2
    rivers = []

    def appendRiver(i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != 1:
            return 0
        else:
            matrix[i][j] = index
            return 1 + appendRiver(i-1, j) + appendRiver(i, j-1) + appendRiver(i+1, j) + appendRiver(i, j+1)

    for i, row in enumerate(matrix):
        for j, _ in enumerate(row):
            river = appendRiver(i, j)
            if river > 0:
                rivers.append(river)

    return rivers
