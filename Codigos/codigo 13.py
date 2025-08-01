from random import randint
numero_random = randint(1,10)
print('Adivina el numero aleatorio')
usuario = int(input('Ingresa un numero: '))
while usuario != numero_random:
    if usuario >= numero_random:
        print("Estas muy cerca pero es menor al numero que ingresaste")
        usuario = int(input("Intenta otra vez: "))
    elif usuario <= numero_random:
        print("Estas muy cerca pero es mayor al numero que ingresaste")
        usuario = int(input("Intenta otra vez: "))

print("Ganaste, Felicidades")

        


    




