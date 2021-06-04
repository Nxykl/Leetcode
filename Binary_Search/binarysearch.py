def binsry_search(nums, target):
    i = 0
    j = len(nums)-1

    while i < j:
        mid = (i + j)//2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            i +=1

        elif nums[mid]> target:
            j -=1

    return -1


nums = [1,2,3,4,5]
target = 4
print(binsry_search(nums, target))

