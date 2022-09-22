from numpy import prod

def main():
    string_numeros, lista_numeros = solicitar_numeros()

    producto = multiplicar(lista_numeros)

    print("El string ingresado fue: \"" + string_numeros + "\" y la multiplicacion de los numeros ingresados es: " + str(producto))
 
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

#Creamos una funcion que multiplique los elementos de la lista 
def multiplicar(lista_numeros):
    
    lista_producto = prod(lista_numeros)

    return lista_producto
    

if __name__ == "__main__":
    main()