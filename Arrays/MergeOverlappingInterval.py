def mergeIntervals(int):

    newInterval = []
    int.sort()

    for i in range(len(int)):
        if len(newInterval) == 0 or newInterval[-1][1] < int[i][0]:
            newInterval.append([int[i][0],int[i][1]])
        else:
            newInterval[-1][1] = max(newInterval[-1][1],int[i][1])




    return newInterval



intervals = [[1,3],[4,5],[3,4]]
print(mergeIntervals(intervals))