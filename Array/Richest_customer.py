
def richest(nums):
    maxi = 0
    for item in nums:
        sum = 0
        for j in item:
            sum += j
        maxi = max(maxi, sum)
    return maxi



nums = [[1,2,3],[3,2,1]] # return 6
acc = [[1,5],[7,3],[3,5]] # return 10
print(richest(acc))