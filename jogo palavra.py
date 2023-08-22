import random


def embaralha(palavra):
    p_embaralhada = random.sample(palavra, len(palavra))
    return ''.join(p_embaralhada)


l = ["python", "renata", "faculdade", "computador", "tecnologia", "informação"]
chances = 6
psorteada = random.choice(l)
p_embaralhada = embaralha(psorteada)

while chances !=0:
    print(p_embaralhada)
    resposta = input('Tente advinhar a palavra ->  ')
    if resposta == psorteada:
        print(f'Você acertou a palavra!!! {psorteada}')
        break
    else:
        chances = chances -1
        if chances == 0:
            print(f'Você perdeu!!!! A palavra sorteada era -> {psorteada}')
        else:
            print('Você errou a palavra sorteada!')
            print(f'Você ainda tem {chances} chances para jogar!')






