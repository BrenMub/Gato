def main(): 

    string_numeros, lista_numeros = solicitar_numeros()
    nueva_lista = intercambiar(lista_numeros)

    print("El string ingresado fue: \"" + string_numeros + "\" y la nueva lista es: " + str(nueva_lista))


#Creamos una funcion que solicite los numeros al usuario y maneje excepciones
def solicitar_numeros():

    son_validos = False 

    while son_validos == False:
        print("Inserte numeros de la siguiente forma: 34,2,7,8")

        try:
            string_numeros = input("Digite una serie de numeros separados por comas: ")
            numeros = convertir_a_int(string_numeros)
        except: 
            print("Algún valor ingresado no es valido")
        else: 
            son_validos = True 
        
    return string_numeros, numeros
            
#Creamos una funcion que convierta el string a una lista de numeros                
def convertir_a_int(string_numeros):
    
    lista_numeros = [int(i) for i in string_numeros.split(",")]

    return lista_numeros 


def intercambiar(lista_numeros):

    #Guardamos en una variable temporal el primer elemento y cambiamos la primera posicion por la ultima y despues la ultima por la primera
    primer_elemento = lista_numeros[0]
    lista_numeros[0] = lista_numeros[-1]
    lista_numeros[-1] = primer_elemento

    return lista_numeros


if __name__ == "__main__":
    main()