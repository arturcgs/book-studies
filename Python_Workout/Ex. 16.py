

def dictdiff(d1, d2):
    dic_diff = {}
    #first going through the first dict, d1
    for key, d1_value in d1.items():
        d2_value = d2.get(key, None) #getting the value for d2
        if d1_value != d2_value: #if the values are different, I create a list with them
            dic_diff[key] = [d1_value, d2_value]

    #now doing the same thing, but going through d2
    for key, d2_value in d2.items():
        if dic_diff.get(key, False): #checking if I already saved that key when going through d1
            continue
        d1_value = d1.get(key, None)
        if d1_value != d2_value:
            dic_diff[key] = [d1_value, d2_value]

    return dic_diff

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d1, d1))
print(dictdiff(d1, d2))

d3 = {'a':1, 'b':2, 'd':3}
d4 = {'a':1, 'b':2, 'c':4}
print(dictdiff(d3, d4))

d5 = {'a':1, 'b':2, 'd':4}
print(dictdiff(d1, d5))