HRPD=int(input('quantas horas esse funcionario trabalha por dia?'))
DMT= int(input('quantos dias no mês esse funcoionario trabalhou?'))
VPM=float(input('quanto esse funcionario gamha por dia?'))
porcemtagem=10/100
Valor_ganho_por_hora= VPM/HRPD
Valor_bruto_por_mês= Valor_ganho_por_hora*HRPD*DMT
Valor_comicional_do_funcionario=Valor_bruto_por_mês*porcemtagem
Valor_liquido_por_mês=Valor_bruto_por_mês+Valor_comicional_do_funcionario

print ('Esse funcionario ganha no mês: ', Valor_liquido_por_mês)