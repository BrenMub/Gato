def main():
    imprimir_figura()

#Imprimimos la figura 
def imprimir_figura():

    #Este for se encarga de la cantidad de filas que tiene la figura
    for i in range(1,10):

        #Realizamos dos for dependiendo del valor de i pues la figura cuando llega a 5 asteriscos en una misma linea empieza a decrecer la cantidad de estos

        if i < 6:
            for j in range(i):
                print ('* ', end="") 
        else:
            for j in range(i,10):
                print ('* ', end="") 

        print("")

if __name__ == "__main__":
    main()
