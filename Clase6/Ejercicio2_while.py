numero_1 = int(input('Digite un numero entero: '))

contador = 0
suma = 0

while contador <= numero_1:
    #print(contador)
    suma += contador
    contador += 1

print('La suma es: ' + str(suma))