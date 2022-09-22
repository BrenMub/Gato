def main():

    #Se solicitan los datos al usuario
    palabra = input("Digite una palabra: ")
    letra = input("Digite una letra: ")

    print(determinar_si_esta(palabra, letra))


#Determina si la letra esta en la palabra o no 
def determinar_si_esta(string, letra):

    if letra in string:
        return True
    else:
        return False

if __name__ == "__main__":
    main()