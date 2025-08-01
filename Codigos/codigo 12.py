
def generar_lista():
    lista = [];
    for numeros in range(1,21):
        lista.append(numeros);
    return lista;


def randome(lista):
    from random import sample
    lista = sample(lista,5)
    
    return lista;


nueva = randome(generar_lista())

print(nueva)

    




