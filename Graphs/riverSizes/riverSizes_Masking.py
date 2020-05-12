#!/usr/bin/python3

import copy
from typing import List

def isNexIndex(point: List[List[int]]):
    return True if point[0][0] == 0 and point[0][1] == 0 and point[1][0] == 0 and point[1][1] == \
                   1 else False

def isCopyAtDown(point: List[List[int]]):
    return True if point[0][0] == 0 and point[0][1] == 0 and point[1][0] == 1 and point[1][1] == 1 else False

def isCopyAtRight(point: List[List[int]]):
    return True if point[0][0] == 0 and point[0][1] == 1 and point[1][0] == 0 and point[1][1] == 1 else False

def isSummary(point: List[List[int]]):
    return True if point[0][0] == 0 and point[0][1] == 1 and point[1][0] == 1 and point[1][1] == 1 else False

def isNewIndexWithTwo(point: List[List[int]]):
    return True if point[0][0] == 1 and point[0][1] == 0 and point[1][0] == 0 and point[1][1] == 1 else False

def isCopyTheWhole(point: List[List[int]]):
    return True if point[0][0] == 1 and point[0][1] == 1 and point[1][0] == 1 and point[1][1] == 1 else False

def isCopyHorizontalCopy2(point: List[List[int]]):
    return True if point[0][0] == 1 and point[0][1] == 0 and point[1][0] == 1 and point[1][1] == 1 else False

def isVerticalCopy2(point: List[List[int]]):
    return True if point[0][0] == 1 and point[0][1] == 1 and point[1][0] == 0 and point[1][1] == 1 else False

def riverSizes(matrix):
    indexes = []
    matrixCopy = copy.deepcopy(matrix)
    riverWeights = {}
    sameNumbers = {}

    for i, row in enumerate(matrixCopy):
        for j, elem in enumerate(row):
            window = [
                [0 if j == 0 else matrixCopy[i - 1][j - 1], matrixCopy[i - 1][j]] if i != 0 else [0, 0],
                [0 if j == 0 else matrixCopy[i][j - 1], matrixCopy[i][j]]
            ]
            if isNexIndex(window):
                if len(indexes) == 0:
                    indexes.append(1)
                    riverWeights.update({1: 0})
                else:
                    indexes.append(indexes[-1] + 1)
                    riverWeights.update({indexes[-1]: 0})
                matrix[i][j] = indexes[-1]
                riverWeights[matrix[i][j]] += 1
            if isCopyAtDown(window) or isCopyHorizontalCopy2(window):
                matrix[i][j] = matrix[i][j - 1]
                riverWeights[matrix[i][j]] += 1
            if isCopyAtRight(window) or isVerticalCopy2(window):
                matrix[i][j] = matrix[i - 1][j]
                riverWeights[matrix[i][j]] += 1
            if isSummary(window):
                if matrix[i][j - 1] not in sameNumbers.keys() and matrix[i - 1][j] not in sameNumbers.keys():
                    for key, value in sameNumbers.items():
                        if matrix[i - 1][j] in value:
                            value += [matrix[i - 1][j]]
                            value += [matrix[i][j - 1]]
                    sameNumbers.update({matrix[i][j - 1]: [matrix[i - 1][j]]})
                elif matrix[i - 1][j] in sameNumbers.keys():
                    sameNumbers[matrix[i - 1][j]] += [matrix[i][j - 1]]
                else:
                    sameNumbers[matrix[i][j - 1]] += [matrix[i + 1][j]]
                matrix[i][j] = matrix[i][j - 1]
                riverWeights[matrix[i - 1][j]] += 1
            if isNewIndexWithTwo(window):
                indexes.append(indexes[-1] + 1)
                matrix[i][j] = indexes[-1]
                riverWeights.update({indexes[-1]: 1})
            if isCopyTheWhole(window):
                matrix[i][j] = matrix[i][j - 1]
                riverWeights[matrix[i][j - 1]] += 1

    if sameNumbers:
        vals = []
        for key, value in sameNumbers.items():
            for v in value:
                if v in sameNumbers.keys():
                    vals.append(v)
                    value += sameNumbers.get(v)
		for d in vals:
            del sameNumbers[d]
        for a, b in riverWeights.items():
            for c, d in sameNumbers.items():
                if a in d:
                    riverWeights[c] += riverWeights[a]
        for x in sameNumbers.values():
            for y in list(set(x)):
                del riverWeights[y]
        return [i for i in riverWeights.values()]
    else:
        return [i for i in riverWeights.values()]

