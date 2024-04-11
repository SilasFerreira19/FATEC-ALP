encerrar = False
numero_tentativas = 0
ldt = 0
ndni = 0
print('Bem-vindo ao jogo de Adivinhação')
nepju = int(input('Escolha um número jogador 1 (1 a 10): \n'))
while nepju < 1 or nepju > 10:
    ndni += 1
    print('Número Invalido!')
    nepju = int(input('Escolha um número jogador 1 (1 a 10): \n'))
    if ndni == 10:
        print('Você digitou o um número errado muitas vezes')
        break
else:

    while encerrar == False:
        nepjd = int(input('Agora é sua vez jogador 2, tente adivinhar 0 número escolhido pelo jogador 1: \n'))
        numero_tentativas += 1
        if nepjd != nepju:
            ldt += 1
            print('Número errado!')
        if ldt == 9:
            print('Você perdeu burrão, tentou mais de 8 vezes!')
            break
        elif nepjd == nepju:
            if numero_tentativas > 1:
                print(f'Parabéns, você acertou em {numero_tentativas} tentativas')
            else:
                print(f'Parabéns, você acertou em {numero_tentativas} tentativa')
            break