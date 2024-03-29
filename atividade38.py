horas=int(input('Digite a hora:'))
minutos= int(input('Digite os minutos'))
segundos= int (input('Digite os segundos'))
tempo_de_duração= int(input('Digite quanto tempo durou a operação em minutos'))
utimos_segundos= horas*3600+minutos*60+segundos
tempo_de_duração_S=(tempo_de_duração//60)
tempo_total= utimos_segundos+tempo_de_duração_S
horas_finais=(tempo_total//3600)%24
minutos_finais=(tempo_total % 3600)//60
segundos_finais=segundos % 60
print (f"O horario final será:{horas_finais}:{minutos_finais}:{segundos_finais}")