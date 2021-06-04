
# without recursion
def insertion_sort(arr):

    for index in range(len(arr)):
        value = arr[index]
        j = index

        while j > 0 and arr[j-1] > value:
            arr[j] = arr[j-1]
            j=j-1

        arr[j] = value

    return arr

#with recursion

def insertion_recursive(arr, i, length):
    value = arr[i]
    j = i

    while j >0  and arr[j-1] > value:
        arr[j] = arr[j-1]
        j = j-1

    arr[j] = value

    if i+1 <= length:
        insertion_recursive(arr, i+1, length)






arr = [3,8,5,4,1]
#cp_arr = insertion_sort(arr)
i =1
length = len(arr)-1
insertion_recursive(arr,i, length)

print(arr)
