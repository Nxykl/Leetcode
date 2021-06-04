

def Selection_Sort(nums):

    for i in range(len(nums)):

        min = i

        for j in range(i+1,len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[min],nums[i] = nums[i],nums[min]

    return nums






nums = [3,5,8,4,1,9,-2]

print(Selection_Sort(nums))