def main():
    string_numeros, lista_numeros = solicitar_numeros()

    lista_duplicados = crear_lista_duplicados(lista_numeros)

    print("El string ingresado es: " + string_numeros + " ,la lista que contiene unicamente a los duplicados es: " + str(lista_duplicados) )

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

#Creamos una funcion que crea una lista con los elementos duplicados 
def crear_lista_duplicados(lista_numeros):

    nueva_lista = []
    for i in lista_numeros:

        #Se verifica que sea un numero que este mas de una vez y que no se encuentre en la nueva lista
        if lista_numeros.count(i) > 1 and i not in nueva_lista:
            nueva_lista.append(i)
    
    return nueva_lista

if __name__ == "__main__":
    main()