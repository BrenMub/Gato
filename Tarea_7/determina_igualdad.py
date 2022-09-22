def main():

    string_tupla = solicitar_numeros()

    tupla = convertir_a_tupla(string_tupla)

    print("La tupla ingresada es: " + str(tupla) + " y " + determinar_igualdad(tupla))

def solicitar_numeros():

    print("Debe ingresar los numeros con este formato \" 2,5,6,7 \"")
    string_tupla = input("Digite los numeros de la tupla: ")


    return string_tupla

def convertir_a_tupla(string_tupla):

    lista = [int(x) for x in string_tupla.split(",")] 
 
    return tuple(lista)

def determinar_igualdad(tupla):

    if tupla.count(tupla[0]) == len(tupla):
        return "todos los elementos en la tupla son iguales"
    else:
        return "existe al menos un elemento en la tupla que no es igual al resto"


if __name__ == "__main__":
    main()