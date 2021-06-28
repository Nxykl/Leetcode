def max_Sum(arr, window_size):

    window_sum = sum([arr[i] for i in range(window_size)])
    max_sum = window_sum

    for index in range(len(nums) - window_size):
        window_sum = window_sum - arr[index] + arr[index+window_size]
        max_sum = window_sum

    return max_sum






nums = [1,2,100,-1,5]
window_size = 3

print(max_Sum(nums, window_size))