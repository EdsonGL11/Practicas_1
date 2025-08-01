numero = int(input("Ingresa un número para mostrar su tabla de multiplicar: "))

print(f"\nTabla de multiplicar del {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
