def media_corrida():
    total = 0
    i = 0
    while True:
        n = input('Enter the 10 km run time: ', end='a')

        if not n:
            print('<enter>')
            break

        total += float(n)
        i += 1

    print(f'\nAvarage of {total / i}, over {i} runs')

media_corrida()

#Extra 1
import math

def antes_depois():
    numero = float(input('Choose a number: '))
    antes = int(input('How many number before the point do you want? '))
    depois = int(input('How many number after the point do you want? '))

    numero_antes = math.floor(numero % (10 ** antes))
    numero_depois = (math.floor((numero % 1) * (10 ** depois))) / (10 ** depois)

    print(f'{numero_antes + numero_depois}')

antes_depois()

#Extra 2
from decimal import Decimal
def soma_correta_float():
    numero1 = input('First Number to be added: ')
    numero2 = input('Second Number to be added: ')
    soma = Decimal(numero1) + Decimal(numero2)
    print(soma)

soma_correta_float()






