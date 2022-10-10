from sys import *
def maxProfit(nums):
    profit = 0
    buy = maxsize
    sell = 0

    for i in range(len(nums)):
        if nums[i] < buy:
            buy = nums[i]
            sell = nums[i]
        if nums[i] > buy :
            sell = nums[i]
        profit = max(profit , sell - buy)


    return profit

stocks = [1,3,0,2,1,3,2,5,9]
print(maxProfit(stocks))