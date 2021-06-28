
# Brute Force solution
def running_sum(nums):
    new_nums = []

    for i in range(len(nums)):
        sum = 0
        for j in range(0, i+1):
            sum += nums[j]
        new_nums.append(sum)

    return new_nums



#nums = [1,2,3,4] # return [1,3,6,10]
nums = [1,1,1,1,1]

print(running_sum(nums))