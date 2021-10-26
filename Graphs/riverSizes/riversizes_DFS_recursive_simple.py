def river_sizes_dfs(matrix):
    rivers = []

    def append_river(i, j):
        if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and matrix[i][j] == 1:
            matrix[i][j] = 0
            return 1 + append_river(i - 1, j) + append_river(i, j - 1) + append_river(i + 1, j) + append_river(i, j + 1)
        return 0

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                rivers.append(append_river(i, j))

    return rivers
