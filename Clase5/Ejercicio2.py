nota = float(input("Digite la nota del estudiante "))

if nota < 70:
    if nota >= 60 and nota < 70:
        print("El estudiante debe ir a convocatoria")
    else: 
        print("El estudiante reprobo el curso")
else: 
    print("El estudiante aprueba el curso")
    