from collections import Counter

def most_repeating_word(words_list): #I did this one
    lista = [Counter(word).most_common(1)[0][1] for word in words_list]
    return words_list[lista.index(max(lista))]

def most_repeating_word_2(words_list): #This is the solution from the book
    return max(words_list, key=lambda x: Counter(x).most_common(1)[0][1])



word_list = ['bttttttttttttt', 'estranho', 'entender', 'bagaceiraa', "aaaaaaa"]
print(most_repeating_word(word_list))
print(most_repeating_word_2(word_list))

'''Beyond 1
Instead of finding the word with the greatest number of repeated letters, find
the word with the greatest number of repeated vowels'''

def most_repeated_vowel(word):
    most_common = (0,0)
    for letter in Counter(word).most_common():
        if letter[0] in 'aeiou':
            most_common = letter
            break
    return most_common[1]

def most_vowels(words_list):
    return max(words_list, key=most_repeated_vowel)

print(f'most vowels - {most_vowels(word_list)}')

'''Beyond 2
Write a program to read /etc/passwd on a Unix computer. The first field contains
the username, and the final field contains the user’s shell, the command interpreter. 
Display the shells in decreasing order of popularity, such that the most popular shell is 
shown first, the second most popular shell second, and so forth.'''

