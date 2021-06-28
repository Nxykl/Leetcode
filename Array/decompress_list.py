def decompress(nums):
    new_lis = []
    for i in range(len(nums)//2):
        freq = nums[2*i]
        for j in range(freq):
            val = nums[2*i+1]
            new_lis.append(val)
    return new_lis


nums = [1,2,3,4]
print(decompress(nums))
