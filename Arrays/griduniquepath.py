"""
Brute Force - Time limit exceeded
"""

def noofuniquepaths(arr, i, j, m, n, count):

    if arr[i][j] != 1:
        if j < n - 1:
            count = noofuniquepaths(arr, i, j + 1, m, n, count)
        if i < m - 1:
            count = noofuniquepaths(arr, i + 1, j, m, n, count)
    else:
        return count + 1
    return count


def griduniquepaths(m, n):
    arr = [[0 for x in range(n)] for y in range(m)]
    arr[m-1][n-1] = 1

    return noofuniquepaths(arr, 0, 0, m, n, 0)

"""
Time Complexity - exponential
sc - exponential
"""



def calculate(m,n,i,j):

    if i == m - 1 and j == n - 1:
        return 1
    if i >= m or j >= n:
        return 0
    else:
        return calculate(m,n,i, j + 1) + calculate(m,n,i+1,j)



def griduniquepaths2(m,n):
    return calculate(m,n,0,0)


def calculatedp(m,n,i,j,dp):

    if i == m - 1 and j == n - 1:
        return 1
    if i >= m or j >= n:
        return 0
    if dp[i][j] != 0:
        return dp[i][j]
    else:
        dp[i][j] = calculatedp(m,n,i, j + 1,dp) + calculatedp(m,n,i+1,j,dp)
        return dp[i][j]


def griduniquepathsdp(m,n):

    dp = [[0 for x in range(n)] for y in range(m)]

    num = calculatedp(m,n,0,0,dp)
    if m == 1 and n == 1: return num
    return dp[0][0]

m, n = 1,1
print(griduniquepathsdp(m, n))


