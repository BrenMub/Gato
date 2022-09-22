def main():

    print("Los primeros 7 múltiplos de 7 son: " , end = "" )
    calcular_multiplos_de_7()

#Creamos una funcion que imprime los primeros 7 multiplos de 7
def calcular_multiplos_de_7():
    for i in range(8):
        print(7*i, end = " ")

if __name__ == "__main__":
    main()