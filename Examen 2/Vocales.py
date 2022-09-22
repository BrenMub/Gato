def main():

    palabra = input("Digite una palabra: ")
    print(f"La cantidad de vocales que tiene la palabra {palabra} es: {cantidad_vocales(palabra)}")

def cantidad_vocales(string):
    
    contador = 0
    vocales = "aeiou"

    #Se itera por cada letra y se compara con cada uno de las del string vocales, i.e. con cada vocal
    for letra in string:
        for vocal in vocales:
            if vocal == letra:
                contador += 1

    return contador

if __name__ == "__main__":
    main()