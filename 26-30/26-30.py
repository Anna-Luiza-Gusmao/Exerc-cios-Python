"""
# 26
m2 = float(input("Digite o valor em metros quadrados: "))
print(f'Valor convertido em hectares: {m2 * 0.0001}')

# 27
h = float(input("Digite o valor em hectares: "))
print(f'Valor convertido em metros quadrados: {h * 10_000}')

# 28
valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))
valor3 = int(input("Digite o valor 3: "))

q_valor1 = valor1 * valor1
q_valor2 = valor2 * valor2
q_valor3 = valor3 * valor3

soma = q_valor1 + q_valor2 + q_valor3
print(f'Soma dos quadrados: {soma}')

# 29
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(media)
"""
# 30
real = float(input("Digite um valor em real: "))
dolar = float(input("Qual a cotação do dólar? "))
print(f'O valor convertido em dólares é: {real * dolar}')
