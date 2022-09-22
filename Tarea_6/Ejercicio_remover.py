def main():

    string_numeros, lista_numeros = solicitar_numeros()

    nueva_lista = remover_numeros(lista_numeros)

    print("El string ingresado fue: \"" + string_numeros + "\" y la nueva lista es: " + str(nueva_lista))


#Creamos una funcion que solicite los numeros al usuario y maneje excepciones
def solicitar_numeros():

    son_validos = False 

    while son_validos == False:
        print("Inserte numeros de la siguiente forma: 34,2,7,8")

        try:
            string_numeros = input("Digite una serie de numeros separados por comas: ")
            lista_numeros = convertir_a_int(string_numeros)
        except: 
            print("Algún valor ingresado no es valido")
        else: 
            son_validos = True 
        
    return string_numeros, lista_numeros
            
#Creamos una funcion que convierta el string a una lista de numeros        
def convertir_a_int(string_numeros):
    
    lista_numeros = [int(i) for i in string_numeros.split(",")]

    return lista_numeros 

#Creamos una funcion que remueva el numero deseado por el usuario de la lista
def remover_numeros(lista_numeros):

    numero = int(input("Digite el numero que desea remover de la lista: "))

    #La nueva lista contiene unicamente los numeros distintos de los ingresados por el usuario
    nueva_lista = list(filter(lambda p : p!= numero, lista_numeros))

    return nueva_lista


if __name__ == "__main__":
    main()