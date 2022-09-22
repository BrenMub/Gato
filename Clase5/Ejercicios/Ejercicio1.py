
def main():
    peso  = float(input("Ingrese su peso en kilogramos "))
    altura = float(input("Ingrese su altura en metros "))
    print("Su indice de masa corporal es: " + str(round(calcular_IMC(peso, altura), 3)) + " y su diagnostico es: " + str(diagnosticar_estado(calcular_IMC(peso, altura)))) 
    print("Recuerde que no es un diagnostico de su estado de salud ya que existen otros factores")

#Calcularmos el IMC del usuario
def calcular_IMC(peso, altura):
    imc = peso/((altura)**2)
    return imc 

#Averiguamos el diagnostico segun el indice de masa corporal del usuario
def diagnosticar_estado(IMC):
    if IMC <= 16:
        return("desnutricion grado 3") 
    elif IMC <= 17:
        return("desnutricion grado 2")
    elif IMC <= 18.5:
        return("desnutricion grado 1")
    elif IMC <= 25:
        return("normal")
    elif IMC <= 30:
        return("sobre peso grado 1")
    elif IMC <= 40: 
        return("sobre peso grado 2")
    else: 
        return("sobre peso grado 3")

if __name__ == "__main__":
    main()


