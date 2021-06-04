def threesum(nums):
    #Brute Force Method with duplicates
    emptyset = set()
    lis = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                sum = nums[i] + nums[j] + nums[k]


                if sum == 0:


    return lis














nums = [-1,0,1,2,-1,-4]
print(threesum(nums))