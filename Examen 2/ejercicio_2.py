#Complete los espacios en blanco dentro de la función smallest_num_list
# para que la función devuelva el número más pequeño que se encuentra en la lista. 

def smallest_num_list( list ):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min
print(smallest_num_list([5, 8, -8, 0]))
