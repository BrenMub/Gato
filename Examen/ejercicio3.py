#-----------------------------------------#
# Ejercicio 3
# Explicar donde esta el error en este codigo
#-----------------------------------------#

# Problema

numero = input("inserte numero ")
print(type(numero)) #Note que la entrada es un string por lo que nunca entraria al if
if numero == 1: 
    print("Llegue aqui")

#Existen dos soluciones
# La primera es fila 8 cambiar input("inserte numero ") por int(input("inserte numero "))
# La segunda es en la fila 10 colocar if numero == "1"