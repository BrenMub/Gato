def main():
    keys = ['make', 'model', 'price']
    values = ['Toyota','Yaris', 17800]

    print(convertir_listas_a_diccionario(keys, values))


def convertir_listas_a_diccionario(keys, values):
    diccionario = {}
    for i in range(len(keys)):
        diccionario[keys[i]] = values[i]
    
    return diccionario


if __name__ == "__main__":
    main()