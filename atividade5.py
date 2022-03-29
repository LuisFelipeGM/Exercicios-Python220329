print("Algoritmo para ver a cotação do dolar e converter em real!\n")

cotd = float(input("Digite a cotação do Dólar: "))
qtdd = int(input("Digite a quantidade de Dólares desejado: "))

precor = cotd * qtdd

print(f"\nA cotação do Dólar é: US${cotd}\nA Quantidade de Dólares desejada é: {qtdd}")
print(f"O valor dessa compra em reais é de: R${precor:.2f}")