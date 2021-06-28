def first_occurance(nums, target):
    left = 0
    right = len(nums)-1
    result = 0
    while left < right:
        mid = (left + right)//2

        if nums[mid] ==  target:
            result = mid
            right -=1

        elif nums[mid] < target:
            left = left +1

        else:
            right -=1

    return result

def last_occurance(nums, target):
    left = 0
    right = len(nums)-1
    result = 0
    while left < right:
        mid = (left + right)//2

        if nums[mid] ==  target:
            result = mid
            left +=1

        elif nums[mid] < target:
            left = left +1

        else:
            right -=1

    return result





nums = [2,5,5,5,6,6,8,9,9,9,9]
target = 5
fst_ocr = first_occurance(nums, target)
lst_ocr = last_occurance(nums, target)
count = (lst_ocr - fst_ocr)+1

print("count of occurance ", count)
print("The first occurance in index ", fst_ocr)
print("The last occurance in index ", lst_ocr)