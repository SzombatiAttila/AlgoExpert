#!/usr/bin/python3

def riverSizes(matrix):
    visitedMatrix = [[False for i in x] for x in matrix]
    blobs = []

    def riverSizesRec(mat, visMatrix, i, j, blobs, counter, unvisitedNeighbours=[], neighbours=[]):
        visMatrix[i][j] = True
        counter += 1
        if [i, j] not in unvisitedNeighbours:
            neighbours = [[i, j]]
        for x in range(i - 1, i + 2):
            for y in range(j - 1, j + 2):
                if -1 < x < len(mat) and -1 < y < len(mat[0]):
                    if [x, y] not in [[i - 1, j - 1], [i + 1, j - 1], [i - 1, j + 1], [i + 1, j + 1], [i, j]]:
                        if not visMatrix[x][y]:
                            visMatrix[x][y] = True
                            neighbours.append([x, y])
        for neighbour in neighbours:
            unvisitedNeighbours.append(neighbour)
        while len(neighbours):
            currentPoint = neighbours.pop()
            if not visMatrix[currentPoint[0]][currentPoint[1]]:
                continue
            if mat[currentPoint[0]][currentPoint[1]] == 1:
                if 0 < counter:
                    riverSizesRec(mat, visMatrix, currentPoint[0], currentPoint[1], blobs, counter, unvisitedNeighbours,
                                  neighbours)
        blobs.append(counter - 1)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1 and not visitedMatrix[i][j]:
                riverSizesRec(matrix, visitedMatrix, i, j, blobs, counter=0)
    b = []
    c = []
    for i in blobs:
        if i != 0:
            b.append(i)
        else:
            c.append(max(b))
            b = []
    return c
