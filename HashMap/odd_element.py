

def oddElement(nums):

    xor = 0

    for x in nums:
        xor = xor ^ x
        print(xor)

    return xor

nums = [4, 3, 6, 2, 6, 4, 2, 3, 4, 3, 3]
print(oddElement(nums))
