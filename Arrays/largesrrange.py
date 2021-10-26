def largest_range(array):
    ranges = []
    visited_array2 = [False for _ in array]

    def largest_ranges(arrays, visitedArray, point, pointsArray):
        if array[point] - 1 in array and not visitedArray[array.index(array[point] - 1)]:
            largest_ranges(arrays, visitedArray, array.index(array[point] - 1), pointsArray)
        if visitedArray[point]:
            return 0
        visitedArray[point] = 1
        pointsArray.append(arrays[point])
        if arrays[point] + 1 in arrays:
            largest_ranges(arrays, visitedArray, arrays.index(arrays[point] + 1), pointsArray)
        if not len(ranges):
            ranges.append(pointsArray)
        elif ranges[0][-1] - ranges[0][0] < pointsArray[-1] - pointsArray[0]:
            return pointsArray

    for i in range(len(array)):
        if not visited_array2[i]:
            largest_ranges(array, visited_array2, point=i, pointsArray=[])
    return [ranges[0][0], ranges[0][-1]]
