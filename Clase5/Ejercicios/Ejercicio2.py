
def main():
    print("Recuerde que una funcion cuadratica es de la forma a^2x + bx + c, donde el primer coeficiente es a, el segundo es b y el tercero c")
    coeficente_1 = float(input("Digite el primer coeficiente de la ecuacion cuadratica"))
    coeficiente_2 = float(input("Digite el segundo coeficiente de la ecuacion cuadratica"))
    coeficiente_3 = float(input("Digite el tercer coeficiente de la ecuacion cuadratica"))
    print("El discriminante de la ecuación donde a = " + str(coeficente_1) + " ,b = " + str(coeficiente_2) + " y  c = " + str(coeficiente_3) + " es: " + str(calcular_discriminante(coeficente_1, coeficiente_2, coeficiente_3)))

#Calculamos el discriminante
def calcular_discriminante(coeficiente_1, coeficiente_2, coeficiente_3):
    discriminante = coeficiente_2**2 - (4*coeficiente_1*coeficiente_3)
    return discriminante

if __name__ == "__main__":
    main()