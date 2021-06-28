
def array_sorted_or_not(arr):
    for i in range(len(arr)):
        if not arr[i] < arr[i+1]:
            return False
        else:
            return True


nums = [ 20, 20, 78, 98, 99, 97]
print(array_sorted_or_not(nums))