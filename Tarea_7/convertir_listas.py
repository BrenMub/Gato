def main():

    lista_original_tuplas = [(11, 12), (56, 32), (78, 44)]

    print("Al convertir las tuplas a lista se obtiene: " + str(convertir_tuplas(lista_original_tuplas)))


def convertir_tuplas(lista):

    lista_tuplas = []

    for tupla in lista:
        lista_tuplas.append(list(tupla))

    return lista_tuplas



if __name__ == "__main__":
    main()