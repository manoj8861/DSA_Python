#traverse array from end and get index where elements starts to decrease
# for the element in that index look for element greater than that in the remaining array and swap it
# sort the remaining array  and return it

#if elements are in descending order from end then arrange it in arranging order and return it


def nextpermutation(num):
    i  = j = len(num) -1
    while num[i-1] >= num[i] and i > 0:
        i -= 1
    if i == 0 :
        num.reverse()
        return
    k = i - 1

    while num[j] <= num[k]:
        j -= 1
    num[j],num[k] = num[k],num[j]
    l,r = k + 1,len(num)-1
    while l< r:
        num[l],num[r] = num[r],num[l]
        l += 1
        r -= 1




inp = [1,4,3,2]
nextpermutation(inp)
print(inp)