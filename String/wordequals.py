def fn1(s1, s2, target):
    def fn(word):
        ans = 0
        for i in word:
            print(i)
            ans *= 10
            ans += ord(i)-ord('a')


        return ans
    #res1 = fn(s1)
    #res2 = fn(s2)
    #print(res2)
    res3 = fn(target)
    #print(res1)
    print(res3)
    return res3


s1 = "aaa"
s2 ="a"
target = "aab"
print(fn1(s1,s2,target))