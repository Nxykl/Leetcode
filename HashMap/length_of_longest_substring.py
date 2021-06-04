
def Length_Substring(s):

    hashmap ={}
    start=0
    end=0

    for i in range(len(s)):

        if s[i] in hashmap and start <= hashmap[s[i]]:
            print(hashmap[s[i]], s[i])
            start = hashmap[s[i]] +1
        else:

            end = max(end, i-start+1)
            print(f"end {end}")
        hashmap[s[i]] = i
        print(hashmap[s[i]], i, s[i])

    return end







s = "abcabcbb"
#s = "bbbbb"
print(Length_Substring(s))