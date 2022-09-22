#-----------------------------------------#
# Ejercicio 4
# Imprimir las tablas de multiplicar del 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#-----------------------------------------#

# Problema

for x in range(11):
    print()
    print("Tabla del " + str(x ) + "\n")
    for j in range(11):
       print(str(x) + "*" + str(j) + " = " + str(x*j))
    
