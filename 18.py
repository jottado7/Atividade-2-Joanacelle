a = int(input("Digite um número: "))

if (a == 0):
    print("Neutro")
elif (a % 2 == 0) and (a > 0):
    print("Par positivo")
elif (a % 2) == 0 and (a < 0):
    print("Par negativo")
elif (a % 2 != 0) and (a > 0):
    print("Ímpar positivo")
else:
    print("Ímpar negativo")