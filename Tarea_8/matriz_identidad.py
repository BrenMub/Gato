def main():
    print("En caso de que desee una matriz 3x3 debe digitar que la dimension de la matriz es 3.")
    dimension = int(input("Digite la dimension de la cual desea que sea la matriz: "))

    print("La matirz identidad de dimension " + str(dimension) + "x" + str(dimension) + " es:" + str(crear_matriz_identidad(dimension)))


def crear_matriz_identidad(dimension):

    matrices_nulas = [ [0 for j in range(dimension)] for x in range(dimension)]

    for i in range(dimension):
        matrices_nulas[i][i] = 1

    return matrices_nulas


if __name__ == "__main__":
    main()