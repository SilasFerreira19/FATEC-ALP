dia = int(input("Insira um número que represente um dia da semana: "))

match dia:
    case 1: print('Domingo')
    case 2: print('Segunda')
    case 3: print('Terça')
    case 4: print('Quarta')
    case 5: print('Quinta')
    case 6: print('Sexta')
    case 7: print('Sabado')
    case _: print('Número Invalido')