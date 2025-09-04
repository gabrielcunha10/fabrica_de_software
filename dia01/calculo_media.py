nota1, nota2, nota3 = map(float,input("Digite as suas três notas:\n").split())
nota1 *= 2
nota2 *= 5
nota3 *= 6
resultado = (nota1 + nota2 + nota3) / 13
print(f"A sua média é {resultado:.2f}")