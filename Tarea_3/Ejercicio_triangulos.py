def main(): 

    #Creamos un arreglo con los lados
    lados = pedir_numeros()

    print(determinar_tipo(lados))

def pedir_numeros():
    #Declaramos esta variable como falsa para ingresar al while
    son_positivos = False 

    #Verificamos que los numeros ingresados sean mayores a 0
    while son_positivos == False:
        
        try:
            lado_1 = int(input("Digite el valor del primer lado: "))
            lado_2 = int(input("Digite el valor del segundo lado: "))
            lado_3 = int(input("Digite el valor del tecer lado: "))
        except:
            print("Algún valor ingresado no es valido")
        else:
            #Verificamos que los numeros ingresados sean positivos
            if lado_1 > 0 and lado_2 > 0 and lado_3 > 0:
                #Verificamos que los valores ingresados puedan formar un triangulo
                if es_triangulo([lado_1, lado_2, lado_3]):
                    son_positivos = True
                else:
                    print("Los lados ingresados no conforman un triangulo")
                    print("Recuerda que la suma de los dos lados mas pequenos debe ser mayor o igual al lado mas grande")
            else:
                print("Los lados no pueden ser menores o iguales a 0")

    return [lado_1, lado_2, lado_3]

#Verificamos que los valores ingresados puedan formar un triangulo (la suma de los dos lados mas pequenos sea mayor o igual que el lado mas grande)
def es_triangulo(lados):

    #Creamos otra lista con los lados ingresados por el usuario ordenada de menor a mayor
    lados_ordenados = sorted(lados)

    if (lados_ordenados[0] + lados_ordenados[1] >= lados_ordenados[2]):
        return True
    else:
        return False

#Determinamos el tipo del triangulo formado con los valores ingresados
def determinar_tipo(lados):

    #Si los 3 lados son iguales es equilatero
    if lados.count(lados[0]) == 3:
        return("El triangulo es equilatero")  

    #Si dos lados son iguales es isoseles
    elif lados.count(lados[0]) == 2 or lados.count(lados[1]) == 2:
        return("El triangulo es isoseles")

    #si todos los lados son distintos es escaleno
    else:
        return("El triangulo es escaleno")

if __name__ == "__main__":
    main()