numero=int(input('Digite um valor inteiro.'))
horas= numero//3600
minutos= numero//60
segundos=numero % 60

print(f'o valor em horas será: {horas}:{minutos}:{segundos}.')