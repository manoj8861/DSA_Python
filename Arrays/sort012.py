def sortnumbers(nums):
    low = 0
    mid = 0
    high = len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            mid += 1
            low += 1
        elif nums[mid] ==1:
            mid += 1
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1

lst = [0,0,1,2,2,1,0,2,1,2,1]
sortnumbers(lst)
print(lst)