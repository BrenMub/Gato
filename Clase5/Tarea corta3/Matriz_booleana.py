def main():
    matriz = crear_matriz_booleana()

    #Esta lista contiene la posicion de las filas del ejercicio 2
    lista_1 = [0,0,0,1,1,1,2,3,3,4,4,4]
    #Esta lista contiene la posicion de las columnas del ejercicio 2
    lista_2 = [1,3,4,0,2,4,1,0,4,0,1,3]

    matriz_true = volver_true_casillas(lista_1,lista_2, matriz)

    print( matriz_true)
    print(f"Existen {determinar_amigos(matriz_true)} parejas de amigos en la matriz")

    numero_fila, numero_columna = solicitar_numeros()

    set = determinar_amigos_comunes(numero_fila, numero_columna, matriz_true)

    print(informar(numero_fila, numero_columna, set ))



#Ejercicio 1

#Esta funcion crea una matriz 5x5 llena de False
def crear_matriz_booleana():

    matriz_booleana = [ [False for j in range(5)] for x in range(5)]

    return matriz_booleana


#Ejercicio 2

#Esta funcion convierte en true las casillas que el ejercicio indica
def volver_true_casillas(lista_1, lista_2, matriz):

    for i in range(len(lista_1)):
        matriz[lista_1[i]][lista_2[i]] = True 
    return matriz 

#Ejercicio 3

#Esta funcion determina la cantidad de pareja de amigos que hay en la matriz
def determinar_amigos(matriz):
    
    contador = 0
    for i in range(5):
        for j in range(5):
            if matriz[i][j] == True and matriz[j][i] == True and i != j:
                contador += 1
    
    return contador//2

#Ejercicio 4

#Esta funcion se encarga de solicitar los numeros de los que el usuario desea conocer si tiene amigos en comun 
def solicitar_numeros():

    print("\nDigite dos numeros enteros en el intervalo [0,4], donde el primero corresponde al numero de fila de la matriz y el segundo al numero de la columna")
    print("Los numeros se solicitan para conocer si esa entrada de la matriz tiene amigos en comun")

    numero_1 = int(input("Digite el primer numero: "))
    numero_2 = int(input("Digite el segundo numero: "))

    return numero_1, numero_2

def determinar_amigos_comunes(numero_fila, numero_columna, matriz):

    set_amigos_1 = set()
    set_amigos_2 = set()

    if matriz[numero_fila][numero_columna] == True:
        
        for i in range(5):

            #Esta condicion determina los amigos del primer valor ingresado por el usuario
            if (matriz[numero_fila][i] == True or matriz[i][numero_fila] == True):
                set_amigos_1.add(i)

            #Esta condicion determina los amigos del segundo valor ingresado por el usuario
            if (matriz[numero_columna][i] == True or matriz[i][numero_columna] == True):
                set_amigos_2.add(i)

        #Se realiza una interseccion porque se buscan los amigos en comun 
        set_amigos_1 = set_amigos_1.intersection(set_amigos_2)      

        #Se asegura de que un numero no sea amigo en comun de el mismo
        set_amigos_1.discard(numero_fila)
        set_amigos_1.discard(numero_columna)

        return set_amigos_1
    
    else:
        return set_amigos_1

#Esta funcion informa sobre la cantidad de amigos en comun entre los dos valores ingresados
def informar(numero_fila, numero_columna, set):

    string = ""
    if len(set) == 0:
        return f"Los numeros {numero_fila} y el {numero_columna} no tienen amigos en comun"

    else:
        for i in set:
            string += str(i) + "," 

        string_final = string[:-1]
    
    return f"Los numeros que tienen en comun el {numero_fila} y el {numero_columna} son: {string_final}"
            

if __name__ == "__main__":
    main()