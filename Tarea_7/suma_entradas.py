
def main():

    lista_tuplas =  [(11, 22, 66), (21, 13, -6), (31, 34), (21, 21, 21, 21)]

    print("La suma de la tupla en la n-esima posicion es la entra n-esima de la siguiente tupla: " + str(sumar_tuplas(lista_tuplas)))


def sumar_tuplas(lista_tuplas):

    lista_suma = []
    suma = 0
    for tupla in lista_tuplas:
        for elemento in tupla:  
            suma += elemento

        lista_suma.append(suma)
        suma = 0 

    return tuple(lista_suma)

if __name__ == "__main__":
    main()