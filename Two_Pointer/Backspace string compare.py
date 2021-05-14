def backspacecompare(s, t):
    s_lis = []
    t_lis = []
    for i in s:
        if i == "#" and len(s_lis) !=0:
            s_lis.pop()
        elif i != "#":
            s_lis.append(i)

    for j in t:
        if j == "#" and len(t_lis) != 0:
            t_lis.pop()
        elif j != "#":
            t_lis.append(j)

    if len(s_lis) != len(t_lis):
        return False
    else:
        for k in range(len(s_lis)):
            if s_lis[k] != t_lis[k]:
                return False

    return True

#t = "ad#c"
#s = "ab#c"
#s = "ab##"
#t = "c#d#"
#s = "a#c"
#t = "b"
s = "a##c"
t = "#a#c"
print(backspacecompare(s, t))

