# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("# OUTPUT ESPERADO: ")

km = float(input("por quantos dias o carro foi alugado: "))
dias = float(input("por quantos km o carro rodou: "))

preco = (dias * 60 + km * 0.15)

print(f"você andou {km}km por {dias}dias , entao o preço a pagar é R${preco:.2f} ")