nome=input("qual o nome do vendedor")
carros_vendidos_no_mes=float(input('quantos carros esse vendeodr vendeu em um mês'))
valor_da_vende_dos_veicolos=float(input('qual valr agregado na compra dos carros'))

bonificação1= carros_vendidos_no_mes*50
bonificação2= valor_da_vende_dos_veicolos*0.5
salario=500
total= bonificação1+bonificação1+salario
print (f'SR {nome} vendeu {carros_vendidos_no_mes} veicolos e recebeu no mês {total}')