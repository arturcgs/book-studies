
def alpha_sentence(sentence):
    return ','.join(sorted(sentence.split()))

sentence = 'Tom Dick Harry'
print(alpha_sentence(sentence))


def last_word(sentence):
    return sorted(sentence.split(), key=str.lower)[-1]

sentence = 'Which is the last word, alphabetically, in a text file'
print(last_word(sentence))


def longest_word(sentence):
    list = sentence.lower().split()
    longest_word = ''
    for word in list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

print(longest_word(sentence))