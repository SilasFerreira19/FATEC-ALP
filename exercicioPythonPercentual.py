salariodocara = float(input("Informe seu salário: "))
percent = float(input("Informe o percentual de aumento(0 a 100): "))

if (percent >= 0 and percent <= 100):
    percentform = percent / 100
    salarioform = salariodocara * percentform
    salariototal = salariodocara + salarioform

    print("Com o aumento de ",percent,"% Seu salario atual é R$",salariototal," \nO aumento foi de R$",salarioform)
else:
    print("Percentual Invalido!")