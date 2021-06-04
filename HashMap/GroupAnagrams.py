
def GroupAnagrams(s):

    hashmap = {}
    for i in range(len(s)):
        ls = sorted(s[i])
        x =''.join(sorted(ls))
        

        if x in hashmap:
            print(s[i], hashmap[x])


        hashmap[x] = s[i]



s = [
        "CARS", "REPAID", "DUES", "NOSE", "SIGNED", "LANE",
        "PAIRED", "ARCS", "GRAB", "USED", "ONES", "BRAG",
        "SUED", "LEAN", "SCAR", "DESIGN"]

GroupAnagrams(s)

