
def twosum(nums, target):

    hashmap = {}

    for i,n in enumerate(nums):
        if target-n in hashmap:

            a = [hashmap[target-n], i]

            return a
        hashmap[n] = i


nums = [2,7,11,15]
target = 9
print(twosum(nums, target))
