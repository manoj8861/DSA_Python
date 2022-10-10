# naive approach

# Uses O(N) space

def findduplicate(nums):

    dst = {}
    for i in range(len(nums)):
        if nums[i] not in dst:
            dst[nums[i]] = i
        else:
            return nums[i]

    return False


# Optimized apprach

# Floyd's Tortoise and hare method || Twp pointers method

# TC = O(N) sc  = O(1)

def findduplicateTH(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:break

    fast = nums[0]

    if slow != fast:
        slow,fast = nums[slow],nums[fast]

    return slow

lst = [4,4,2,3,1]
print(findduplicateTH(lst))