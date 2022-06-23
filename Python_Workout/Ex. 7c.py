
def translate_URL(URL):
    printable = 'abcdefghijklmnopqrstuvwxyz1234567890%'
    URL_translated = URL
    for character in URL:
        if character not in printable:
            URL = URL.replace(character, f'%{hex(ord(character))[-2:]}')
    return URL

URL = input('Qual a URL: ')
print(translate_URL(URL))

