#Problem : Given a matrix if an element in the matrix is 0
# then you will have to set its entire column and row to 0 and then return the matrix.

#1. Traverse through each element in matrix and check for zero (two loops) - O(M* N)
#2. if zero change its entire row elements and column elements to -1 other than 0 , check previous row and column
# and check next row and column  - O(M)+O(N)
#3. Finally, Traverse entire matrix and set element to 0 if element is -1

#TC - O((M*N)*(M + N))
#SC - O(1)


def SetMatrixZeroBruteForce(a,r,c):
    for m in range(r):
        for n in range(c):
            if a[m][n] == 0:

                ind = m -1
                while ind  >= 0:
                    if a[ind][n] != 0:
                        a[ind][n] = -1
                    ind -= 1

                ind = m + 1
                while ind < r:
                    if a[ind][n] != 0:
                        a[ind][n] = -1
                    ind += 1

                ind = n - 1
                while ind  >= 0:
                    if a[m][ind] != 0:
                        a[m][ind] = -1
                    ind -= 1

                ind = n + 1
                while ind < column:
                    if a[m][ind] != 0:
                        a[m][ind] = -1
                    ind += 1

    for m in range(r):
        for n in range(c):
            if a[m][n] <= 0:
                a[m][n] = 0


#method - 2
#Instead of changing entire row and column keep dummy array for row and column
#if either row element or column element is zero make that element zero

#TC - O(N*M + N*M)
#SC - O(N) or O(M)

def SetMatrixZeroOptimal(a,r,c):
    dummy1 = [-1 for i in range(r)]
    dummy2  = [-1 for i in range(c)]
    for m in range(r):
        for n in range (c):
            if a[m][n] == 0:
                dummy1[m] = 0
                dummy2[n] = 0

    for m in range(r):
        for n in range(c):
            if (dummy2[n] == 0 or dummy1[m] == 0):
                a[m][n] = 0

from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    n = len(matrix)
    m = len(matrix[0])

    rowarr = [-1 for x in range(n)]
    columnarr = [-1 for y in range(m)]

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rowarr[i] = 0
                columnarr[j] = 0

    for i in range(n):
        for j in range(m):
            if (rowarr[i] == 0 or columnarr[j] == 0) :
                matrix[i][j] = 0


if __name__ == "__main__":
    a =[[0, 2,3],[1, 0,3],[1,2, 0]]


    row = len(a)
    column = len(a[0])

    #SetMatrixZeroBruteForce(a,row,column )

    #SetMatrixZeroOptimal(a,row,column)
    setZeros(a)
    for i in range(row) :
        for j in range(column) :
            print(a[i][j],end= " ")
        print()