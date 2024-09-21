#farinha
print("FARINHA")
farinha_qtd = 1000
farinha_prc = 10
farinha_ut = 500
#acucar
acucar_qtd = 1000
acucar_prc = 10
acucar_ut = 300
#ovos
ovo_qtd = 12
ovo_prc = 8
ovo_ut = 4
#leite
leite_qtd = 1000
leite_prc = 7
leite_ut = 200
#manteiga
manteiga_qtd = 500
manteiga_prc = 12
manteiga_ut = 100
#fermentoinput
fermento_qtd = 50
fermento_prc = 5
fermento_ut = 10
#essencia
essencia_qtd = 80
essencia_prc = 11
essencia_ut = 10
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