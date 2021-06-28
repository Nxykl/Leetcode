
# Brute Force Solution
def shuffle_array(nums,n):
    new_list = []
    j = n
    for i in range(n):
        new_list.append(nums[i])
        new_list.append(nums[j])
        j +=1


    return new_list


nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle_array(nums, n))