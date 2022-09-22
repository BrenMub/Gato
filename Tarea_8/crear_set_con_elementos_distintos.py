def main():
    print("Ingrese un set de la siguiente forma \"1,2,3,4\"")
    string_1 = input("Ingrese el primer set: ")
    string_2 = input("Ingrese el segundo set: ")

    print("Al restar ambos sets se obtiene como resultado: " + str(crear_nuevo_set(string_1, string_2)))

def crear_nuevo_set(string_1, string_2):
    set_1 = {int(x) for x in string_1.split(",")}
    set_2 = {int(x) for x in string_2.split(",")}

    
    set = set_1.difference(set_2)

    return set

if __name__ == "__main__":
    main()
