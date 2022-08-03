# beyond 1
'''Iterate over the lines of a text file. Find all of the words (i.e., non-whitespace
surrounded by whitespace) that contain only integers, and sum them.'''


def add_numbers_in_text_file(file_path):
    with open(file_path) as f:
        total = 0
        for line in f:
            for word in line.split():
                if word.isnumeric():
                    total += int(word)
        return total


print(f"Beyond 1: {add_numbers_in_text_file('files/texto.txt')}\n")

# beyond 2
'''Create a text file (using an editor, not necessarily Python) containing two tabseparated columns, 
with each column containing a number. Then use Python
to read through the file you’ve created. For each line, 
multiply each first number by the second, and then sum the results from all the lines. Ignore any line
that doesn’t contain two numeric columns.'''
import math


def multiplies_and_adds_tab_separated_txt(file_path):
    with open(file_path) as f:
        total = []
        for line in f:
            line_numbers = [int(number) for number in line.split('\t') if number.strip().isnumeric()]
            if line_numbers:
                total.append(math.prod(line_numbers))
        return sum(total)


print(f'Beyond 2: {multiplies_and_adds_tab_separated_txt("files/tab_numbers.txt")}\n')

# beyond 3
'''Read through a text file, line by line. Use a dict to keep track of how many times
each vowel (a, e, i, o, and u) appears in the file. Print the resulting tabulation. '''

from collections import Counter


def count_vowels(phrase):
    counter = Counter({'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0})
    for letter in phrase:
        if letter.lower() in 'aeiou':
            counter[letter.lower()] += 1
    return counter


def txt_vowel_counter(file_path):
    with open(file_path) as f:
        total = Counter()
        for line in f:
            num_vowels = count_vowels(line)
            total = total + num_vowels
        return total


vowels = txt_vowel_counter('files/texto.txt')

print("Beyond 3: ", end='')
for key, item in vowels.items():
    print(f'{key}: {item} | ', end='')
