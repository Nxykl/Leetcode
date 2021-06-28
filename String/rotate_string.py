
def check_str_rotated(str1, str2):
    '''
    temp =0
    for i in range(len(str1)):
        if str1[i] == str2[0]:
            temp = i

    for j in range(len(str2)):
        if str2[j] != str1[temp]:
            return False
        if temp == len(str1)-1:
            temp = 0
        else:
            temp +=1

    return True '''

    str = str1 + str1
    print(str.count(str2))



    if str.count(str2) > 0:
        return 1
    else:
        return 0


str1 = "AACD"
str2 = "ACDA"

print(check_str_rotated(str1, str2))
