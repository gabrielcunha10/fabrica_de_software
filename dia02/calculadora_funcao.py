historico = ["Histórico:"]
def calculadora(historico):
    continuar = True
    while continuar:
        try:
            num1, num2 = map(int,input("Digite dois números para efetuar a conta e tecle ENTER:\n").split())
        except ValueError:
            print("Digite dois números separados por espaço.\n")
            continue
        operacao = input("Escolha qual a operação você deseja usar (+) para soma, (-) para subtração, (*) para multiplicação e (/) para divisão:\n").upper()
        if operacao == "+":
            print(f"{num1} {operacao} {num2} = {num1 + num2}")
            historico.append(f"Soma - {num1} {operacao} {num2} = {num1 + num2}")
        elif operacao == "-":
            print(f"{num1} {operacao} {num2} = {num1 - num2}")
            historico.append(f"Subtração - {num1} {operacao} {num2} = {num1 - num2}")
        elif operacao == "*":
            print(f"{num1} {operacao} {num2} = {num1 * num2}")
            historico.append(f"Multiplicação - {num1} {operacao} {num2} = {num1 * num2}")
        elif operacao == "/":
            if num2 == 0:
                print("Divisão por zero não é permitido.")
                continue
            print(f"{num1} {operacao} {num2} = {num1 / num2}")
            historico.append(f"Divisão - {num1} {operacao} {num2} = {num1 / num2}")
        else:
            print("Escolha uma das quatro opções (+, -, *, /).")
            continue
        decisao = input("Deseja continuar? S/N\n").upper()
        if decisao == "S":
            continuar = True
            continue
        else:
            continuar = False
            break
    print(historico)
calculadora(historico)