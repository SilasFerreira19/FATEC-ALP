encerrar = False
numero_tentativas = 0
ldt = 0
print('Bem-vindo ao jogo de Adivinhação')

while True:
    try:
        nepju = int(input('Escolha um número jogador 1 (1 a 10): \n'))
        if 1 <= nepju <= 10:
            break
        else:
            print('Número Inválido!')
    except ValueError:
        print('Número Inválido!')

while not encerrar:
    try:
        nepjd = int(input('Agora é sua vez jogador 2, tente adivinhar o número escolhido pelo jogador 1: \n'))
        numero_tentativas += 1
        if nepjd != nepju:
            ldt += 1
            print('Número errado!')
        if ldt == 9:
            print('Você perdeu burrão, tentou mais de 8 vezes!')
            encerrar = True
        elif nepjd == nepju:
            print(f'Parabéns, você acertou em {numero_tentativas} tentativas')
            encerrar = True
    except ValueError:
        print('Número Inválido!')
