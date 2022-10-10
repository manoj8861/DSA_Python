#brute force
#TC - o(n * n)
#SC - O(N* N)

def rotateMatrix(nums):
    row = len(nums)
    col = len(nums[0])
    tmatrix = [[0 for _ in range(row)] for _ in range(col) ]
    for i in range(row):
        for j in range(col):
            tmatrix[j][row-1-i] = nums[i][j]
    return tmatrix


#Better Approach

def rotateMatrix2(nums):
    row = len(nums)
    col = len(nums[0])

    #Transpose matrix - change rows into column and vice-versa

    for i in  range(row):
        for j in range(i):
            nums[i][j],nums[j][i] = nums[j][i],nums[i][j]

    for i in range(row):
        nums[i].reverse()




lst = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#print(rotateMatrix(lst))

rotateMatrix2(lst)
print(lst)