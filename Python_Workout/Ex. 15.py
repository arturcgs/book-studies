
def get_rainfall():
    rainfall = {}
    while True:
        city = input('Enter a city name: ').strip()

        if not city:
            break

        rain = int(input("How much rain has fallen in that city: "))

        if city not in list(rainfall.keys()):
            rainfall[city] = [rain]
        else:
            rainfall[city].append(rain)

    for city, rain_list in rainfall.items():
        print(f'{city} --> total: {sum(rain_list)} average: {sum(rain_list) / len(rain_list)}')

#get_rainfall()

#beyond 3
text = '''
Read through a text file on disk. Use a dict to track how many words of each
length are in the file—that is, how many three-letter words, four-letter words,
five-letter words, and so on. Display your results. 
'''

def len_count(text):
    text_list = text.split()
    word_len_count = {}
    for word in text_list:
        word_len_count[len(word)] = word_len_count.get(len(word), 0) + 1
    #printing outcome
    for key in sorted(word_len_count):
        print(f'Word lenght: {key} | Number os appearances: {word_len_count[key]}')

len_count(text)
