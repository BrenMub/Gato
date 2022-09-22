def main():

    tupla_1 = (11, 22, 34, 4)
    tupla_2 = (35, 5, 12, 1)
    tupla_3 = (12,23, 31, 11)

    print("El resultado de sumar las tuplas es: " + str(sumar_tuplas(tupla_1, tupla_2, tupla_3)))


def sumar_tuplas(tupla_1, tupla_2, tupla_3):

    tupla_final = []
    for i in range(len(tupla_1)):
        entrada = tupla_1[i] + tupla_2[i] + tupla_3[i]
        tupla_final.append(entrada)

    return tuple(tupla_final)   

if __name__ == "__main__":
    main()