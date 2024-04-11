kmp = float(input("Digite o valor de quilometros percorrido: "))
lg = float(input("Digite o valor em litros de combustível gasto: "))

tcc = kmp / lg

print("A taxa de consumo é igual a",tcc,"km/l")    
if tcc <= 8:
    print("A taxa de consumo está ALTA")
elif tcc > 8:
    print("A taxa de consumo está BAIXA")