#-----------------------------------------#
# Ejercicio 1
# Maquina de voltaje 
#-----------------------------------------#

# Problema

maquinaPrendida = True
voltaje = 0
while(maquinaPrendida):
    voltaje = voltaje + 1
    # Inserte algun bloque de codigo que haga que la maquina se apague cuando el voltaje supere los 100 voltios
    if voltaje == 100:
        maquinaPrendida = False 

# # Resultado deberia ser 100
print(voltaje)
