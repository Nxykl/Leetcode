def product_subset(arr):
    n = len(arr)
    maxi = 1

    if n == 0:
        return maxi
    else:
        prev = maxi
        maxi = max(prev * arr[0], prev)
        print(prev * arr[0])

        return product_subset(arr[2:])

nums = [-6, 4, -5, 8, -10, 0, 8 ]
print(product_subset(nums))