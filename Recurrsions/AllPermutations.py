def AllPermuatationsRecur(ind,a, ans):

    if ind == len(a):
        ans.append(a.copy())
        return

    for i in range(ind,len(a)):
        a[ind],a[i] = a[i],a[ind]
        AllPermuatationsRecur(ind +1,a,ans)
        a[i],a[ind] = a[ind],a[i]

ans = []
data = [1,2,3,4]

AllPermuatationsRecur(0,data,ans)
print(ans)