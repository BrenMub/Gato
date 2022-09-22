#-----------------------------------------#
# Ejercicio 2
# Sumar los los numeros pares del 1 al 5
#-----------------------------------------#

# Problema

sumatoria = 0
for x in range(6):                   #__ que llegue al numero 10 __: PREGUNTAR
    if(x%2 == 0):                     #_ validar valores pares _ ):
        sumatoria += x                #__realizar una sumatoria__
print(sumatoria)
