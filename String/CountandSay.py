from collections import Counter

def countandsay(input, length):
    if length == 0:
        return
    for key, value in Counter(input).items():




st = "1121"
for key, value in Counter(st).items():
    new_str = str(value) + str(key)
    print(new_str)
