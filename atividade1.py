print("Algoritmo para calcular Salário\n")
htr = int(input("Quantas Horas você trabalha? "))
vhr = float(input("Quanto custa cada hora de trabalho? "))

sl = htr * vhr

print ("Você trabalhou: " + str(htr) + " Horas\nCada hora vale: " + str(vhr) + " Reais\nLogo seu salário será:" , sl)