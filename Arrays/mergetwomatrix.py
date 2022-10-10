#merge two sorted arrays without extra space
#brute force
#tc = O(n * m)
#sc = O(1)

def merge(a1,a2):
    for i in range(len(a1)):
        if a1[i] > a2[0]:
            a1[i] ,a2[0] = a2[0],a1[i]

            key = 0
            for i in range(1,len(a2)):
               if a2[i] <= a2[key]:
                   a2[i],a2[key] = a2[key],a2[i]
                   key = i

arr1 = [1,3,4,7,8,9,11]
arr2 = [1,8,9,10,17]
merge(arr1,arr2)
print(arr1)
print(arr2)