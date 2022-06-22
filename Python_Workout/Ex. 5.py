
def pig_latin(palavra):

    palavra = palavra.lower()

    #verificando se tem pontuação no final e tirand se tiver
    pontuacao = False
    if palavra[-1] in "!?.,;:":
        pontuacao = palavra[-1]
        palavra = palavra[:-1]

    #se começa com vogal
    if palavra[0] in 'aeiou':
        palavra_lp = palavra + 'way'

    #se palavra começa com consoante
    else:
        palavra_lp = palavra[1:] + palavra[0] + 'ay'

    #adicionando a pontuação de novo no final
    if pontuacao:
        palavra_lp = palavra_lp + pontuacao

    return palavra_lp.title()

palavra = input('Qual a palavra: ')
print(pig_latin(palavra))


