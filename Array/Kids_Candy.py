def kids_with_max_candy(nums, candy):

    maxi = max(nums)
    new_lis = []
    for i in range(len(nums)):
        sum = nums[i] + candy

        if sum == maxi or sum >= maxi:
            new_lis.append(True)
        else:
            new_lis.append(False)
    return new_lis


candies = [2,3,5,1,3]
extraCandies = 3
print(kids_with_max_candy(candies, extraCandies))
