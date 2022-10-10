# Majority in Array by floor(N/2)

# Brute - O(N^2) - two iterations over array to find element > n//2

# better - TC - O(N) And SC - O(N) use of hashmap

def findmajority(nums):
    hashmap = {}
    for i in nums:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            hashmap[i] = hashmap[i] + 1

        if hashmap[i] > len(nums)//2:
            return i



    return 0


# Optimal Moore voting Algorithm  TC - O(2N) ==> O(N), SC - O(1)

def findmajoritymoore(nums):

    # Find Majority Candidate TC - O(N)

    count = 0
    candidate = 0

    for i in nums:
        if count == 0:
            candidate = i

        if candidate == i:
            count += 1
        else:
            count -= 1

    # Verify count for candidate TC - O(N)

    candidatecount = 0
    for j in nums:
        if j == candidate:
            candidatecount += 1

    if candidatecount > len(nums)//2:
        return candidate


    return 0


arr = [1,2,2,3,2,4,2]
print(findmajority(arr))
print(findmajoritymoore(arr))