def main():

    numero = int(input("Ingrese un numero positivo entero: "))

    print(crear_diccionario(numero))


def crear_diccionario(numero):
    diccionario = {}
    for i in range(numero):
        diccionario[i+1] = (i+1)**2
    return diccionario

if __name__ == "__main__":
    main()