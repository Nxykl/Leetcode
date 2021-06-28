def count_smaller_number(num):

    new_lis = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):

            if j !=i and nums[j] < nums[i]:
                count +=1
        new_lis.append(count)

    return new_lis


nums =  [8,1,2,2,3]
print(count_smaller_number(nums))