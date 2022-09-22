#Solicitamos los datos al usuario
representacion_turno = int(input("Ingrese el numero que corresponde al turno: "))
categoria = int(input("Ingrese la categoria del colaborador: "))
salario = float(input("Ingrese el salario del colaborador: "))

#Verificamos si cumple la opcion 1 o la opcion 2
if representacion_turno == 1: 
    print("Cumple las condiciones para la promocion")
elif categoria == 1 or salario <= 350000: 
    print("Cumple las condiciones para la promocion")
else:
    print("El colaborador no cumple las condiciones para la promocion")