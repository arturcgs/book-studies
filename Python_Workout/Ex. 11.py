import operator

def alphabetize_names(PEOPLE):
    alphabetized_list = []
    for p in sorted(PEOPLE, key=lambda x: [x['last'], x['first']]):
        alphabetized_list.append(p)
    return alphabetized_list

def alphabetize_names_itemgetter(people):
    return sorted(people, key=operator.itemgetter('last', 'first'))

PEOPLE = [{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
          {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
          {'first': 'Vladimir', 'last': 'Putin', 'email': 'president@kremvax.ru'}]

print(alphabetize_names_itemgetter(PEOPLE))

#beyond 1
#Given a sequence of positive and negative numbers, sort them by absolute value
def sort_abs(numbers):
    return sorted(numbers, key = lambda x: abs(x))

numbers = [1, 6, -5, -20, 15, 600, -54]
print(sort_abs(numbers))

#beyond 2
#Given a list of strings, sort them according to how many vowels they contain.
def sort_vowel(strings):
    return sorted(strings, key=lambda x: sum(1 for p in x if p in 'aeiouAEIOU'), reverse=True)

lista = ['batata', 'estranho', 'loucura', 'hhh', 'aaaaaaaaaaaaaaaa']
print(sort_vowel(lista))

#beyond 3
#Given a list of lists, with each list containing zero or more numbers, sort by the
#sum of each inner list’s numbers

def sort_list_sum(list):
    return sorted(list, key=sum)

lista = [[1,2,3], [4,5,6], [0], [500]]
print(sort_list_sum(lista))