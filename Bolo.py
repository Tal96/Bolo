#farinha
print("FARINHA")
farinha_qtd = input("Qual a gramatura do saco da farinha de trigo? ")
farinha_prc = input("Preço da farinha: ")
farinha_ut = input("Quanto você utiliza em um bolo? ")
#acucar
acucar_qtd = input("Qual a gramatura do saco de açucar? ")
acucar_prc = input("Qual a preço do saco de açucar? ")
acucar_ut = input("Qual a gramatura utilizada de açucar para um bolo? ")
#ovos
ovo_qtd = input("Qual a quantidade de ovos comprada? ")
ovo_prc = input("Qual o preço dos ovos? ")
ovo_ut = input("quantos ovos serão utilizados? ")
#leite
leite_qtd = input("Quantos litros de leite vem na caixa:  ")
leite_prc = input("Qual o preço? ")
leite_ut = input("Quanto será utilizado?  ")
#manteiga
manteiga_qtd = input("Qual a gramatura do saco da farinha de trigo? ")
manteiga_prc = input("Qual a gramatura do saco da farinha de trigo? ")
manteiga_ut = input("Qual a gramatura do saco da farinha de trigo? ")
#fermentoinput
fermento_qtd = input("Qual a gramatura do saco da farinha de trigo? ")
fermento_prc = input("Qual a gramatura do saco da farinha de trigo? ")
fermento_ut = input("Qual a gramatura do saco da farinha de trigo? ")
#essencia
essencia_qtd = input("Qual a gramatura do saco da farinha de trigo? ")
essencia_prc = input("Qual a gramatura do saco da farinha de trigo? ")
essencia_ut = input("Qual a gramatura do saco da farinha de trigo? ")
#eletrica
eletrica = 5
#gas
gas = 7
########################################################################################################################
valor_ut_F = (farinha_prc)/(farinha_qtd/farinha_ut)
valor_ut_A = (acucar_prc)/(acucar_qtd/acucar_ut)
valor_ut_O = (ovo_prc)/(ovo_qtd/ovo_ut)
valor_ut_L = (leite_prc)/(leite_qtd/leite_ut)
valor_ut_M =(manteiga_prc)/(manteiga_qtd/manteiga_ut)
valor_ut_FE = (fermento_prc)/(fermento_qtd/fermento_ut)
valor_ut_E = (essencia_prc)/(essencia_qtd/essencia_ut)
valor_total_ut = valor_ut_F + valor_ut_A + valor_ut_O + valor_ut_L + valor_ut_M + valor_ut_FE +valor_ut_E +eletrica + gas

print(f"O valor utilizado para o bolo ser feito é : {valor_total_ut:.2f} Reais")
print(f"Sendo vendido inteiro a : {valor_total_ut*1.5} Reais e por {valor_total_ut*1.5 /12:.2f} a fatia")
#########################################################################################################################
sobra_F =farinha_qtd - farinha_ut
sobra_A = acucar_qtd - acucar_ut
sobra_O = ovo_qtd - ovo_ut
sobra_L = leite_qtd - leite_ut
sobra_M = manteiga_qtd - manteiga_ut
sobra_FE = fermento_qtd - fermento_ut
sobra_E = essencia_qtd - essencia_ut
lista_sobra = [f"Farinha :{sobra_F}", f"Açucar: {sobra_A}", f"Ovos: {sobra_O}", f"Leite: {sobra_L}", f"Manteiga: {sobra_M}", f"Fermento: {sobra_FE}", f"Essencia de Baunilha: {sobra_E}"]

if sobra_F >= farinha_ut and sobra_A >= acucar_ut and sobra_O >= ovo_ut and sobra_L >= leite_ut and sobra_M >= manteiga_ut and sobra_FE >= fermento_ut and sobra_E >= essencia_ut:
    for l in lista_sobra:
        print(l)
    print("Você pode fazer um novo bolo com os ingredientes que sobraram.")

else:
    print("Ingredientes insuficientes.")