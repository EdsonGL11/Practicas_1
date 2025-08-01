def calcular(num):
    if num % 2 == 0:
        return f'el numero {num} es par'
    else: 
        return f'el numero {num} es impar'
    
numero = int(input('Ingresa un numero para averiguar si es impar o par: '))
calculo = calcular(numero)
print(calculo)
