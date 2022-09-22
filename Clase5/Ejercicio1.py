angulo_1 = float(input("Digite el valor del angulo de un triangulo "))
angulo_2 = float(input("Digite el valor del angulo de un triangulo "))
angulo_3 = float(input("Digite el valor del angulo de un triangulo "))

#Verificamos si la suma de los angulos es 180
if (angulo_1 + angulo_2 + angulo_3 ==180):
    print("Con estos angulos podemos formar un triangulo")
else:
    print("Con estos angulos podemos no formar un triangulo")