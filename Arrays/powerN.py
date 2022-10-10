
#Optimal Method
# TC - O(logn)
# sc - O(1)

def calpow(x,n):

    ans = 1
    nn = n
    if nn < 0:
        nn = -1 * nn

    while(nn):
        if nn % 2:
            ans = ans * x
            nn = nn - 1
        else:
            x = x * x
            nn = nn//2

    if n < 0:
        ans = 1/ans

    return ans


print(calpow(4,-2))