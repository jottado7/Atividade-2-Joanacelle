a = input("Digite um valor: ")

try:
    a = float(a)
    print("Tipo numérico")
    print("Quadrado:", a ** 2)
except:
    print("Não é numérico")