num1, num2 = map(int,input("Digite dois números para efetuar a conta e tecle ENTER:\n").split())
operação = input("Escolha qual a operação você deseja usar (Soma, subtração, multiplicação e divisão):\n").upper()
resultado = 0
if operação == "SOMA":
    resultado = num1 + num2
elif operação == "SUBTRAÇÃO":
    resultado = num1 - num2
elif operação == "MULTIPLICAÇÃO":
    resultado = num1 * num2
elif operação == "DIVISÃO":
    resultado = num1 // num2
else:
    print("Escolha uma das quatro opções.")
print(f"A {operação} de {num1} e {num2} é igual à: {resultado}")
