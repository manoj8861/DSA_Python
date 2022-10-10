#Naive Approach
import  sys
#TC - O(N**2)
#SC - O(1)
def getMaxSubArrSum(nums,subArr):
    maxsum = -sys.maxsize

    for i in range(len(nums)):
        sum = 0
        for j in range(i,len(nums)):
            sum = sum + nums[j]
            if maxsum < sum :
                subArr.clear()
                maxsum =sum
                subArr.append(i)
                subArr.append(j)

    return maxsum

#Optimal

def getmaxsarrsum(nums,subArr):

    totalSum = -sys.maxsize
    sum = 0
    start = 0

    for i in range(len(nums)):
        sum = sum + nums[i]
        if sum > totalSum :
            totalSum = sum
            subArr.clear()
            subArr.append(start)
            subArr.append(i)

        if sum < 0:
            sum = 0
            start = i + 1

    return totalSum


subArr = []
lst = [-7 ,-8, -16 ,-4 ,-8 ,-5, -7 ,-11, -10, -12, -4, -6, -4, -16, -10]
#print(getMaxSubArrSum(lst,subArr))
print(getmaxsarrsum(lst,subArr))
print(subArr)
print([lst[x] for x in range(subArr[0],subArr[len(subArr)-1]+1)])