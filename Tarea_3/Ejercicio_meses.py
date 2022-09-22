def main():

    #Numero ingresado por el susuario 
    numero_mes = pedir_numero()

    #Cantidad de dias que tiene el mes correspondiente al numero ingresado
    cantidad_dias = retornar_cantidad_dias(numero_mes)

    print('La cantidad de dias del mes ' + str(numero_mes) + ' es: ' + str(cantidad_dias))


#Creamos una funcion para solicitar valores al usuario
def pedir_numero():

    #Declaramos esta variable como falsa para ingresar al while
    es_valido = False


    while es_valido == False:

        #Realizamos manejo de excepciones
        try:
            numero_mes = int(input('Digite el numero del mes del que desea conocer la cantidad de dias: '))
        except:
            print('El valor ingresado no es valido')
        else:
            #En caso de que el numero ingresado este en el intervalo [1,12] es valido 
            if numero_mes > 0 and numero_mes < 13:
                es_valido = True
            else:
                print('El valor ingresado no corresponde a un mes')

    return numero_mes


#Creamos una funcion que retorne la cantidad de dias del mes correspondiente ingresado por el usuario
def retornar_cantidad_dias(numero_mes):

    #Creamos un diccionario donde las llaves corresponden al numero del mes y los valores a la cantidad de dias del mes
    meses = {
        1 : 31, 
        2: 28, 
        3 : 31, 
        4: 30, 
        5: 31, 
        6: 30, 
        7: 31, 
        8: 31, 
        9: 30, 
        10 : 31, 
        11 : 30, 
        12 : 31
    } 

    cantidad_dias = meses[numero_mes]

    return cantidad_dias 


if __name__ == '__main__':
    main()

