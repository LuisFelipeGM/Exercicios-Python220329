print("Algoritmo para calcular o pagamento de comissão de vendedores\n")

vend = input("Digite o Nome do Vendedor: ")
codp = int(input("Digite o Código do produto: "))
precop = float(input("Digite o preço unitário da peça: "))
quantv = int(input("Digite a quantidade vendida: "))

comi = (precop * quantv) * (5/100)

print(f"\nO vendedor que receberá a comissão é o/a: {vend}\nO total de peças vendidas foi: {quantv}")
print(f"O valor da commisão será {comi}")