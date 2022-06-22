
def firstlast(element):
    return element[:1] + element[-1:]

element = [-5, 6, 94, 'a', ('m', 'o')]
print(firstlast(element))

#beyond 1

def even_odd_sums(element):
    even_sum = 0
    odd_sum = 0
    for index in range(1, len(element), 2):
        even_sum += element[index]
    for index in range(0, len(element), 2):
        odd_sum += element[index]
    return [even_sum, odd_sum]

element = [10, 20, 30, 40]
print(even_odd_sums(element))

#beyond 2

def plus_minus(element):
    total = element[0]
    for index in range(1, len(element)):
        if index % 2 == 1:
            total += element[index]
        else:
            total -= element[index]
    return total

element = [10, 20, 30, 40, 50, 60]
print(plus_minus(element))

#beyond 3

def myzip(*argv):
    list_total = []
    for i in range(0, len(argv[0])):
        list_zip = []
        for j in range(0, len(argv)):
            list_zip.append(argv[j][i])
        list_total.append(tuple(list_zip))
    return list_total

print(myzip([1, 2], (5, 6), 'wo'))