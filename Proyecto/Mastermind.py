def main():

    menu()
    

def menu():

    #Nos indica si ya el juego se ha cargado con anterioridad
    esta_cargado = False 

    #Nos indica si el usuario ha decidido salir del juego
    salir = False

    while salir == False:
        print("1: Cargar codigo")
        print("2: Jugar")
        print("3: Salir")

        #Se realiza manejo de excepciones para los numeros ingresados en la seccion del menu
        try:
            numero_menu = int(input("Si desea realizar alguna de las pasadas acciones digite el numero correspondiente: "))
        except: 
            print("Algún valor ingresado no es valido")
        else: 

            #Se carga el archivo
            if numero_menu == 1:
                lista_resultados = leer_archivo()
                esta_cargado = True
                print("\nEl codigo se ha cargado con exito! \n")
            
            #Se juega Mastermind
            elif numero_menu == 2:

                if esta_cargado == True:
                    jugar(lista_resultados)
                else: 
                    print("\nRecuerde que debe cargar el archivo antes de jugar \n")

            #Se sale del juego
            elif numero_menu == 3:
                salir = True
            
            else:
                print("Debe ingresar un numero entero en el intervalo [1,3]")

    print("\n¡Gracias por jugar!\n")
   


#Esta funcion lee el archivo y retorna los datos en una lista
def leer_archivo():
    
    archivo = open("texto.txt")
    string_resultado = archivo.readline()

    return string_resultado.split(",")


#Esta funcion determina la cantidad de aciertos completos
def aciertos_completos(lista, lista_resultados):
    
    contador = 0
    for i in range(len(lista_resultados)):
        if lista[i] == lista_resultados[i]:
            contador += 1


    return contador 

#Determina la cantidad de aciertos color (no cuenta los aciertos completos)
def aciertos_color(lista, lista_resultados):

    contador = 0
    aciertos_totales = aciertos_completos(lista, lista_resultados)
    copia_lista = lista_resultados.copy()

    for elemento in lista:
        if elemento in copia_lista:
            copia_lista.remove(elemento)
            contador += 1
    
    aciertos_color = contador - aciertos_totales

    return aciertos_color 


#Esta funcion se encarga de que se pueda jugar
def jugar(lista_resultados):

    print("\nPor convencion del juego si desea referirse a alguno de los siguientes colores debe usar su abreviatura R= rojo, A = azul, M = amarillo, V = verde, B = blanco, N = negro \n")
    print("El juego consiste en que debe intentar adivinar los colores ocultos, para ello debe ingresar un string de la siguiente forma \"V,B,N,M\" \n")

    numero_intento = 1

    #Se crea el tablero de juego
    lista_tablero = [ ["X" for j in range(4)] for x in range(10)]

    #Se crea una matriz para que contenga el historial de aciertos
    matriz_aciertos = [ [0 for j in range(2)] for x in range(10)]


    while numero_intento < 11:
        
        print(f"\nIntento: {numero_intento} \n")
        string_prediccion = input("Ingrese su prediccion: ").upper()

        #Se verifica que los valores ingresados sean validos 
        if verificar_valores_string(string_prediccion) == True:

            #Se toman unicamente los primeros 7 caracteres del string ingresado 
            string_final = string_prediccion[:7]
            lista_prediccion = string_final.split(",")

            aciertos_posicion = aciertos_completos(lista_prediccion, lista_resultados)
            print(f"\nAciertos completos: {aciertos_posicion}" )
            
            aciertos_col = aciertos_color(lista_prediccion, lista_resultados)
            print(f"Aciertos color: {aciertos_col}")

            #Si la cantidad de aciertos completos son 4, entonces el usuario ha ganado el juego
            if aciertos_posicion == 4:
                print("\n¡Felicidades, ha ganado el juego!\n")
                print(
                    """
                    ╔═══╗─────────────╔╗───╔╗───╔╗
                    ║╔═╗║────────────╔╝╚╗──║║──╔╝╚╗
                    ║║─╚╬══╦═╗╔══╦═╦═╩╗╔╬╗╔╣║╔═╩╗╔╬╦══╦═╗╔══╗
                    ║║─╔╣╔╗║╔╗╣╔╗║╔╣╔╗║║║║║║║║╔╗║║╠╣╔╗║╔╗╣══╣
                    ║╚═╝║╚╝║║║║╚╝║║║╔╗║╚╣╚╝║╚╣╔╗║╚╣║╚╝║║║╠══║
                    ╚═══╩══╩╝╚╩═╗╠╝╚╝╚╩═╩══╩═╩╝╚╩═╩╩══╩╝╚╩══╝
                    ──────────╔═╝║
                    ──────────╚══╝\n
                    """)
                break

            lista_tablero[10  - numero_intento] = lista_prediccion
            matriz_aciertos[10 - numero_intento] = [aciertos_posicion, aciertos_col]
            tablero_final = retornar_tablero(lista_tablero, matriz_aciertos)

            
            print("La matriz de la izquierda es el tablero del juego")
            print("la matriz de la derecha es el historial de aciertos, donde la primera entrada son los aciertos completos y la segunda los aciertos color\n")
            print(tablero_final)

            numero_intento += 1

            #Si el usuario ha jugado 10 veces y no ha acertado las 4 posiciones, entonces pierde    
            if numero_intento == 11:
                #print("Lo sentimos, ha perdido el juego")
                print(
                    """
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
                    ██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
                    ██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
                    ███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
                    ██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
                    ███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
                    ┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
                    """)

        else:
            print("El string ingresado no es valido")

#Esta funcion se encarga de verificar que el usuario no ingrese predicciones invalidas
def verificar_valores_string(string):
    
    contador = 0
    string_nuevo = string[:7]
    
    letras_validas = "RAMVBN"
    lista_string = string_nuevo.split(",")

    for entrada in lista_string:
        if entrada in letras_validas:
            contador += 1
            
    if len(lista_string) == 4 and contador == 4:
        return True

    else:
        return False                  

#Esta funcion retorna el tablero con las predicciones del usuario y con el historial de aciertos
def retornar_tablero(lista_tablero, lista_aciertos):
    string_tablero = ""

    for i in range(len(lista_tablero)):
    
        string_tablero +=  str(lista_tablero[i]) + "\t" + str(lista_aciertos[i]) + "\n"

    return string_tablero


if __name__ == "__main__":
    main()





