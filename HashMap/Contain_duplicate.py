def contain_duplicates(nums):
    dic = {}

    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    val = list(dic.values())

    for j in val:
        print(j)
        if j >= 2:
            return True
        else:
            return False




nums = [2,14,18,22,22]
print(contain_duplicates(nums))