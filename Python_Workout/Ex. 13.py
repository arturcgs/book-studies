import operator

def format_sort_records(list_tuples):
    list_tuples = sorted(list_tuples, key=operator.itemgetter(1, 0))
    for i in range(0, len(list_tuples)):
        print(f'{list_tuples[i][1]:10}{list_tuples[i][0]:10}{list_tuples[i][2]:5.2f}')

PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

format_sort_records(PEOPLE)

#beyond1
'''If you find tuples annoying because they use numeric indexes, you’re not alone!
Reimplement this exercise using namedtuple objects (http://mng.bz/gyWl),
defined in the collections module. Many people like to use named tuples
because they give the right balance between readability and efficiency.'''

from collections import namedtuple

People = namedtuple('People', ['first', 'last', 'time'])
PEOPLE = [People('Donald', 'Trump', 7.85),
          People('Vladimir', 'Putin', 3.626),
          People('Jinping', 'Xi', 10.603)]

print(PEOPLE[0])