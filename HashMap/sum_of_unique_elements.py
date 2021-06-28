def unique_elements(nums):
    dic = {}
    count = 0
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    for key, value in dic.items():
        print(key, value)
        if value == 1:
            count += key

    return count


nums = [1,2,3,2]
print(unique_elements(nums))