
def remove_duplicates(num):
    j = 0

    for i in range(len(num)):
        if num[i] != num[j]:
            j +=1
            num[j] = num[i]




    return num


num = [1,1,2]
print(remove_duplicates(num))
