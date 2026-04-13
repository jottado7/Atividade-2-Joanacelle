a = int(input("Digite um número: "))
if a == 0:
    print("Neutro")
else:
    if a % 2 == 0:
        tipo = "par"
    else:
        tipo = "impar"
    if a > 0:
        sinal = "positivo"
    else:
        sinal = "negativo"
    print(tipo, sinal)
