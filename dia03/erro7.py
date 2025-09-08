def calcular_media(notas):
    for i in range(4):
        try:
            numero = int(input("Digite uma nota:\n"))
            notas.append(numero)
        except Exception as erro:
            print(f"Verifique se você digitou um número.")
    soma = sum(notas)
    quantidade = len(notas) 
    return soma / quantidade
notas = []
media = calcular_media(notas)
print(f"Média: {media:.2f}")