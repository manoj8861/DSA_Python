# Find majority elements (N//3)

# Since its 1/3 of N there can be max 2 elements which can be majority

# Brute - TC - O(N^2) & sc - O(1)  - 2 Iterations of entire array to find if element count is > N//3

# Better - Hashmap Tc - O(N) & sc - O(N)

# Optimal Approach - Extended Moore Voting Algorithm  - Tc - O(N) sc - O(1)
import sys


def findmajority(nums):
    ans = []

    count1 = 0
    count2 = 0
    cand1 = -sys.maxsize
    cand2 = -sys.maxsize

    for i in nums:
        if i == cand1:
            count1 += 1
        elif i == cand2:
            count2 += 1
        elif count1 == 0:
            cand1 = i
            count1 = 1
        elif count2 == 0:
            cand2 = i
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    v1 = 0
    v2 = 0
    for i in nums:
        if i == cand1:
            v1 += 1
        if i == cand2:
            v2 += 1

    if v1 > len(nums)//3:
        ans.append(cand1)
    if v2 > len(nums)//3:
        ans.append(cand2)

    return ans


arr = [1,2]

print(findmajority(arr))


