def recur_sum_of_array(nums, length):
    if length == 0:
        return 0
    value = recur_sum_of_array(nums[1:], length-1)
    value += nums[0]
    return value

nums=[1,2,3,4,5]
length = 5
print(recur_sum_of_array(nums, length))

