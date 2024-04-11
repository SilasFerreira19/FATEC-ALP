na = 0
ne = 0

print ("Hora de responder")
print("Qual é o nome do planeta de onde o Pequeno Príncipe veio?")
print("A) Terra \nB) Asteróide B-612 \nC) Júpiter \nD) Asteróide B-512")
ac1 = input("Insira a Resposta:")

if ac1 == 'B' or ac1 == 'b':
    na += 1
else:
    ne += 1
print("De quem o Pequeno Príncipe cuidava em seu planeta?")
print("A) Elefante \nB) Carneiro \nC) Rosa \nD) Girafa")
ac2 = input("Insira a Resposta:")

if ac2 == 'C' or ac2 == 'c':
    na += 1
else:
    ne += 1
print("Qual é o primeiro ser vivo que o Pequeno Príncipe conhece quando chega à Terra?")
print("A) A Serpente\nB) A Raposa \nC) O Aviador \nD) A Rosa")
ac3 = input("Insira a Resposta:")

if ac3== 'A' or ac3 == 'a':
    na += 1
else:
    ne += 1
print("O que a Raposa ensina ao Pequeno Príncipe?")
print("A) A dançar \nB) A cantar \nC) A amar \nD) A voar")
ac4 = input("Insira a Resposta:")

if ac4 == 'C' or ac4 == 'c':
    na += 1
else:
    ne += 1
print("O que o Pequeno Príncipe pede ao aviador antes de partir?")
print("A) Que o acompanhe em sua jornada\nB) Que arrume sua nave \nC) Que regue a Rosa \nD) Que cuide da Rosa")
ac5 = input("Insira a Resposta:")

if ac5== 'D' or ac5 == 'd':
    na += 1
else:
    ne += 1
if na == 1:
    print("Parabéns, Você acertou um total de:",na,"Questão!")
else:
    print("Parabéns, Você acertou um total de:",na,"Questões!")
if ne == 1:
    print("Você errou",ne,"Questão")
else:
    print("Você errou",ne,"Questões")

