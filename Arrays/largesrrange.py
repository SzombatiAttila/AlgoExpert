def largestRange(array):
    ranges = []
    visitedArray2 = [False for i in array]
    def largestRanges(arrays, visitedArray, point, pointsArray):
        # Write your code here.
        if array[point] - 1 in array and not visitedArray[array.index(array[point] - 1)]:
            point = array.index(array[point] - 1)
            largestRanges(arrays, visitedArray, point, pointsArray)
        if visitedArray[point]:
            return 0
        visitedArray[point] = True
        pointsArray.append(arrays[point])
        nextPoint = arrays[point] + 1
        if nextPoint in arrays:
            largestRanges(arrays, visitedArray, arrays.index(nextPoint), pointsArray)
        else:
            if 0 == len(ranges):
                ranges.append(pointsArray)
            else:
                maxLenInRanges = max([i[-1] - i[0] for i in ranges])
                if maxLenInRanges < pointsArray[-1] - pointsArray[0]:
                    return pointsArray

    for i in range(len(array)):
        if not visitedArray2[i]:
            largestRanges(array, visitedArray2, point=i, pointsArray=[])
    return [ranges[0][0], ranges[0][-1]]
