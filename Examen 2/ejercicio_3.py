#Complete los espacios en blancos para que la función multiply_list 
# devuelva todos los elementos de la lista multiplicados

def multiply_list(items):
    m_l = 1
    for x in items:
        m_l *= x
    return m_l

print(multiply_list([1,2,-8]))