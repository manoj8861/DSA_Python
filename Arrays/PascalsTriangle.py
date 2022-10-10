#create 2D Array with size of number of rows asked to print
#fill 0th element and last element with 1 for ith row
#for in between rows fill sum of elements from previous row jth element and previous row j-1 th row element




def pascalstriangle(n):
    lst = [[" " for _ in range(n)] for y in range(n) ]
    for i in range(n):
        lst[i][0] = lst[i][i] = 1

        for j in range(1,i):
            lst[i][j] = lst[i-1][j] + lst[i-1][j-1]

    return lst


nrows = 8

pt = pascalstriangle(nrows)
for i in range(nrows):
    for j in range(nrows):
        print(pt[i][j] ,end= " ")
    print()

