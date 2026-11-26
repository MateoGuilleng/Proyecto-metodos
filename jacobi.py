# Metodo iterativo de Jacobi

# Valores iniciales
x = 1
y = 2
z = 2

# Tolerancia (precision)
tol = 0.0001

# Numero maximo de iteraciones
max_iter = 100

# Contador
k = 0

print("Metodo de Jacobi")
print("----------------------------------")

while k < max_iter:

    # Calculamos los nuevos valores usando los valores anteriores
    x_nuevo = (7 + y - z) / 4
    y_nuevo = (21 + 4*x + z) / 8
    z_nuevo = (15 + 2*x - y) / 5

    # Calculamos el error
    error = max(abs(x_nuevo - x),
                abs(y_nuevo - y),
                abs(z_nuevo - z))

    # Actualizamos los valores
    x = x_nuevo
    y = y_nuevo
    z = z_nuevo

    k = k + 1

    print("Iteracion:", k)
    print("x =", x)
    print("y =", y)
    print("z =", z)
    print("Error =", error)
    print("----------------------------------")

    # Condicion de parada
    if error < tol:
        break

print("Solucion aproximada:")
print("x =", x)
print("y =", y)
print("z =", z)
print("Iteraciones realizadas:", k)