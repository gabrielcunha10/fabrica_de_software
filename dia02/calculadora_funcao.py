historico = []
def soma(x,y):
    return x+y
def subtracao(x,y):
    return x-y
def multiplicacao(x,y):
    return x*y
def divisao(x,y):
    return x/y
calculo = True
while calculo:
    num1, num2 = map(int,input("Digite dois números para efetuar a conta e tecle ENTER:\n").split())
    operação = input("Escolha qual a operação você deseja usar (Soma, subtração, multiplicação e divisão):\n").upper()
    resultado = 0
    if operação == "SOMA":
        resultado = soma(num1,num2)
    elif operação == "SUBTRAÇÃO":
        resultado = subtracao(num1,num2)
    elif operação == "MULTIPLICAÇÃO":
        resultado = multiplicacao(num1,num2)
    elif operação == "DIVISÃO":
        if num2 == 0:
            print("Divisão por zero não é permitido.")
        exit()
        resultado = divisao(num1,num2)
    else:
        print("Escolha uma das quatro opções.")
    print(f"A {operação} de {num1} e {num2} é igual à: {resultado:.1f}")
    continuar = input("Deseja continuar? S/N\n").upper()
if continuar == "N":
    calculo = False


    

        


    


    