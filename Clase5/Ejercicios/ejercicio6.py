# ejercicio 6
libros = int(input("ingrese la cantidad de libros"))

#Cada libro cuesta 20 dolares

if libros > 10:
    print("10 de descuento" + str(libros*20*0.90))
elif libros > 30:
    print("20 de descuento" + str(libros*20*0.70))
elif libros > 40:
    print("40 de descuento" + str(libros*20*0.60))
else:
    print(libros*20)


    # ejercicio 6
libros = int(input("ingrese la cantidad de libros"))

# se poseen 20 dolares

if libros < 10:
    print("10 de descuento" + str((libros*20)- (libros *20*0.10)))
elif libros < 30:
    print("20 de descuento" + str((libros*20)- (libros *20*0.30)))
elif libros < 40:
    print("40 de descuento" + str((libros*20)- (libros *20*0.40)))
