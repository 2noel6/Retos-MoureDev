

def colision(a0: tuple, b0: tuple, va: tuple, vb: tuple):
    
    t, a, b = [0, 0], [0, 0], [0, 0]
    solved = False

    # Cálculo de posibles soluciones
    for i in range(2):
        try:
            t[i] = float((b0[i] - a0[i])/(va[i] - vb[i]))
        except ZeroDivisionError:
            t[i] = 0
   
    # Análisis de las posibilidades
    for tiempo in t:
        for i in range(2):
            a[i] = "{:.2f}".format(va[i] * tiempo + a0[i])
            b[i] = "{:.2f}".format(vb[i] * tiempo + b0[i])
        if a == b:
            print(f"Los objetos se cruzarán en el punto: {a} y tardarán {int(tiempo)} unidades de tiempo")
            solved = True
            break
        
    if solved == False:
        print("Los objetos nunca colisionaran")
    


print("\nCaso 1:")        
colision([1, 1], [6, 1], [1, 1], [0, 1])
print("\nCaso 2:")  # b0 + (1, 0)
colision([1, 1], [7, 1], [1, 1], [0, 1])
print("\nCaso 3:")  # b0 + (0, 2)
colision([1, 1], [6, 3], [1, 1], [0, 1])
print("\nCaso 4:")  # vb con movimiento negativo en eje y
colision([1, 1], [6, 1], [1, 1], [0, -1])
print("\nCaso 5:")  # vb con movimiento lento en eje x
colision([1, 1], [6, 1], [1, 1], [0.5, 1])
print("\nCaso 6:")  # colisión con pendientes negativas
colision([8, 8], [8, -1], [-1, -1], [-1, 0])
print("\nCaso 7:")  # colisión con pendientes negativas
colision([3, 2], [5, 1], [2, 4], [1, 3])
# Casos MoureDev
colision((0, 0), (1, 1), (1, 2), (0, 1))
colision((2, 0), (0, 1), (0, 2), (1, 0))
colision((0, 0), (10, 5), (100, 50), (-5, -2.5))