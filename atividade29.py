DT=int(input('Quantos dias esse encanador trabalhou?'))
PDPS= 11/100
PDIR= 8/100
VTDT= (30*DT)
VDPS=VTDT*PDPS
VDIR=VTDT*PDIR
VT=VTDT-VDPS-VDIR
print('O encanador ganhara pelos dias trabalhado', VT)