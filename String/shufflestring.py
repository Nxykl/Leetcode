
def Shuffle_string(str, indices):
    hashmap = {}
    new_str = ""
    for i in range(len(indices)):
        hashmap[indices[i]] = str[i]

    for i in range(len(str)):
        new_str += hashmap[i]

    return new_str

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]

print(Shuffle_string(s, indices))