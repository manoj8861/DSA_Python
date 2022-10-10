def merge(nums,low,mid,high):
    temp =[int() for x in range(100)]
    i = low
    j = mid+1
    k = low
    count = 0
    while (i <= mid and j <= high):
        if nums[i] < nums[j]:
            temp[k] = nums[i]
            i += 1
        else:
            temp[k] = nums[j]
            j += 1

            count = count + mid + 1 - i
        k += 1

    if i > mid:
        while j <= high:
            temp[k] = nums[j]
            j, k = j + 1, k + 1
    else:
        while i <= mid:
            temp[k] = nums[i]
            i,k = i + 1,k + 1

    for f in range(low,high+1,1):
        nums[f] = temp[f]
    return count

def mergesort(nums,low,high):
    count = 0
    if (low < high):
        m = (high + low)//2
        count += mergesort(nums,low,m)
        count += mergesort(nums,m+1,high)
        count += merge(nums,low,m,high)

    return count

list =[5,3,2,1,4]#[1,5,2,7,8,9,3,4,10,3,1000,23,456,123] #
print(mergesort(list,0,len(list)-1))
print(list)