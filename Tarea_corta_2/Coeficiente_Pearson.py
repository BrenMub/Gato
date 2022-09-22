def main():
    string_numeros = solicitar_numeros()

    lista_x, lista_y = convertir_string(string_numeros)

    coeficiente = round(calcular_coeficiente_Pearson(lista_x, lista_y), 2)

    print("El coeficiente de simetria de Pearson mide de la desviación de la simetría, expresada la diferencia entre la media y la mediana con respecto a la desviación estándar del grupo de mediciones")
    
    print("El string ingresado fue: \"" + string_numeros + "\" \nEl coeficiente de Pearson del conjunto de pares ordenados es: " + str(coeficiente))

    explicar_resultado(coeficiente)


#Solicitamos los numeros al usuario
def solicitar_numeros():

    print("Debe ingresar los numeros de la siguiente forma: “3,4; 10,20; 5,7; -11,20; 45,10; -5,-10”")
    string_numeros = input("Digite los puntos de los que desea conocer el coeficiente de Pearson: ")

    return string_numeros

#Obtenemos dos listas, una con las coordenadas del eje x y otra con las del eje y
def convertir_string(string):

    #Esta nueva lista contiene una lista con listas adentro que contienen las coordenadas del punto 
    lista_nueva = [[int(x) for x in i.split(",")]  for i in string.split(";")] 

    #Contiene las coordenadas del eje x
    lista_x = [j[0] for j in lista_nueva]

    #Contiene las coordenadas del eje x
    lista_y = [k[1] for k in lista_nueva]

    return lista_x, lista_y

#Calcula la media de los valores en una lista
def calcular_media(lista):
    
    suma = 0
    for i in lista:
        suma += i

    media = suma/len(lista)

    return media 

#Calcula la desviacion tipica
def calcular_desviacion_tipica(lista):

    #Calcula la sumatoria de cada entrada de la lista al cuadrado
    suma_cuadrada = 0
    for i in lista: 
        suma_cuadrada += i**2

    desviacion_tipica = ((suma_cuadrada/len(lista)) - calcular_media(lista)**2)**(0.5)

    return desviacion_tipica


def calcular_covarianza(lista_1, lista_2):

    suma = 0 
    #Calcula la sumatoria de la multiplicacion de las entradas de la lista (la entrada i con la entrada i de la otra)
    for i in range(len(lista_1)):
        suma += lista_1[i] * lista_2[i]

    covarianza = (suma/len(lista_1)) - (calcular_media(lista_1) * calcular_media(lista_2)) 

    return covarianza

#Calcula el coeficiente de Perason 
def calcular_coeficiente_Pearson(lista_1, lista_2):

    coeficiente = calcular_covarianza(lista_1,lista_2)/(calcular_desviacion_tipica(lista_1) * calcular_desviacion_tipica(lista_2))

    return coeficiente 


def explicar_resultado(numero):

    if numero == -1: 
        print("Existe una correlación negativa perfecta")

    elif numero == 1:
        print("Existe una correlación positiva perfecta")
    
    elif numero == 0: 
        print("No existe relación lineal")
    
    elif numero > 0 and numero < 1:
        print("Existe una correlación positiva")
    
    elif numero < 0 and numero > -1:
        print("Existe una correlación negativa")



if __name__ == "__main__":
    main()