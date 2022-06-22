
def mysum(*item):
    if not item:
        return item
    sum = item[0]
    for arg in item[1:]:
        sum += arg
    return sum

print(f'mysum: {mysum([1, 3], [2, 6])}')

#beyond 1
#precisa arrumar pra funcionar em mais q inteiro
def mysum_bigger_than(threshold, *args):
    if not args:
        return args

    sum = 0
    for arg in args:
        if arg >= threshold:
            sum += arg
    return sum

print(mysum_bigger_than(0, 10, 20, 30))

#beyond 2
def sum_numeric(*args):
    sum = 0
    for arg in args:
        try:
            arg = int(arg)
        except ValueError:
            continue
        sum += arg
    return sum

print(sum_numeric(10, 20, 'a', '30','bcd'))

#beyond 3
#tem q arrumar pra tirar o repetido
def merge_dicts(list):
    merged = list[0]
    for dict in list[1:]:
        for key in dict.keys():
            if key in merged.keys():
                merged[key] = [merged[key], dict[key]]
        merged.update(dict)
    return merged

dict_1 = {'John': 15, 'Rick': 10, 'Misa' : 12 }
dict_2 = {'Bonnie': 18,'Matt' : 16 , 'Rick': 20}
dict_3 = {'Rick': 50, 'Bob': 33}
list = [dict_1, dict_2, dict_3]
print(merge_dicts(list))