arr = [1,3,2,4,1,5]
n = len(arr)
miss = 0
repeat = 0
for i in range(n):
    if arr[abs(arr[i])-1] > 0:
        arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
    else:
        repeat = abs(arr[i])

for i in range(n):
    if arr[i]>0:
        miss = i+1
print("Missing:",miss,"Repeating:",repeat)