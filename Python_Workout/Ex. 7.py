
def ubbi_dubbi(palavra):

    vogal = 'aeiou'
    palavra_traduzida_lista = []

    for letra in palavra:
        if letra in vogal:
            palavra_traduzida_lista.append('ub')
            palavra_traduzida_lista.append(letra)
        else:
            palavra_traduzida_lista.append(letra)

    palavra_traduzida = ''.join(palavra_traduzida_lista)

    return palavra_traduzida

while True:
    palavra = input('Qual a palavra: ')
    print(ubbi_dubbi(palavra))

    if palavra == '0':
        break