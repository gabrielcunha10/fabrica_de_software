def calculo_divisao():
    try:
        num1, num2 = map(int,input("Digite dois números para realizar a divisão:\n").split())
        resultado = num1/ num2
        print(resultado)
    except Exception as erro:
        print(f"Digite os códigos separados por espaço ou verifique-se a divisão não está sendo realizada por 0. {erro}")
calculo_divisao()

