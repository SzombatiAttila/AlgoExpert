def largestRange(array):
    ranges = []
    visitedArray2 = [False for i in array]
    def largestRanges(arrays, visitedArray, point, pointsArray):
    	if array[point] - 1 in array and not visitedArray[array.index(array[point] - 1)]:
    	    largestRanges(arrays, visitedArray, array.index(array[point] - 1), pointsArray)
    	if visitedArray[point]:
    	    return 0
    	visitedArray[point] = 1
    	pointsArray.append(arrays[point])
    	if arrays[point] + 1 in arrays:
    	    largestRanges(arrays, visitedArray, arrays.index(arrays[point] + 1), pointsArray)
    	if not len(ranges):
    	    ranges.append(pointsArray)
    	elif ranges[0][-1] - ranges[0][0] < pointsArray[-1] - pointsArray[0]:
    	    return pointsArray

    for i in range(len(array)):
        if not visitedArray2[i]:
            largestRanges(array, visitedArray2, point=i, pointsArray=[])
    return [ranges[0][0], ranges[0][-1]]
