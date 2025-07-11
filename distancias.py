## Ingresar Coordenadas ##

print('Pon las coordenadas del punto de origen usando el formato x,y: ') 
po = input()
coma_po = po.index(',')  # Encuentra la coma
po_distancia = [po[0:coma_po], po[coma_po+1:]]  # Separa antes y después de la coma

print('Pon las coordenadas del punto final usando el formato x,y: ')
pf = input()
coma_pf = pf.index(',')
pf_distancia = [pf[0:coma_pf], pf[coma_pf+1:]]

## Convertir Texto del Arreglo en Numeros ##

po_int = [int(x) for x in po_distancia]
pf_int = [int(x) for x in pf_distancia]

## Distancia Manhattan ###

dx = pf_int[0] - po_int[0]
dy = pf_int[1] - po_int[1]
manhattan = dx + dy
print(f'Tu distancia manhattan es: {manhattan}')
print()
print()

## Distancia Ecluidiana ###

from math import sqrt
cuadrados = ((dx)**2 + (dy)**2)
raiz = sqrt(cuadrados)
print(f'Tu distancia Euclidiana es: {raiz}')
