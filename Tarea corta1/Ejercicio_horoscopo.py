def main():

    dia = int(input("Digite el dia de su nacimiento: "))
    mes = int(input("Digite el mes de su nacimiento: "))

    

    print("Si su dia de nacimiento es " + str(dia) + " y su mes es " + str(mes) + ", su signo zodiacal es: " + str(determinar_horoscopo(dia, mes)))

def determinar_horoscopo(dia, mes):

    #Creamos un arreglo de listas donde la primera entrada es el dia que termina el horoscopo, la segunda es el mes y la tercera es el signo zodiacal
    horoscopos = [
        [20, 1, "Capricornio"], 
        [19, 2, "Acuario"],
        [20, 3, "Piscis"],
        [20, 4, "Aries"], 
        [21, 5, "Tauro"],
        [21, 6, "Geminis"], 
        [22, 7, "Cancer"],
        [22, 8, "Leo"], 
        [22, 9, "Virgo"],
        [22, 10, "Libra"],
        [22, 11, "Escorpio"], 
        [21, 12, "Sagitario"], 
        [31, 12, "Capricornio"]
    ]

    
    #Se itera campo por campo en el arreglo y se verifica si la fecha ingresada satsiface alguna de las condiciones
    for campo in horoscopos:
        if (campo[1] == mes and campo[0] >= dia) or (campo[1] > mes):
            return campo[2]

        

if __name__ == "__main__":
    main()
