
# METODO ITERATIVO DE JACOBI

# Valores iniciales
x = 1.0
y = 2.0
z = 2.0

# Configuracion
tolerancia = 0.0001
max_iteraciones = 100
k = 0

print("METODO DE JACOBI")
print("=" * 55)

while k < max_iteraciones:

    # Guardamos los valores anteriores
    x_anterior = x
    y_anterior = y
    z_anterior = z

    # Calculamos TODOS los nuevos valores usando
    # exclusivamente los valores anteriores
    x_nuevo = (7 + y_anterior - z_anterior) / 4
    y_nuevo = (21 + 4*x_anterior + z_anterior) / 8
    z_nuevo = (15 + 2*x_anterior - y_anterior) / 5

    # Calculamos el error maximo de esta iteracion
    error = max(
        abs(x_nuevo - x_anterior),
        abs(y_nuevo - y_anterior),
        abs(z_nuevo - z_anterior)
    )

    # Ahora si actualizamos todas las variables
    x = x_nuevo
    y = y_nuevo
    z = z_nuevo

    k += 1

    print(f"\nIteracion {k}")
    print(f"x = {x:.8f}")
    print(f"y = {y:.8f}")
    print(f"z = {z:.8f}")
    print(f"Error = {error:.8f}")

    # Si el error es suficientemente pequeno,
    # detenemos el proceso
    if error < tolerancia:
        print("\nSe alcanzo la tolerancia.")
        break

print("\nRESULTADO FINAL")
print(f"x = {x:.8f}")
print(f"y = {y:.8f}")
print(f"z = {z:.8f}")
print(f"Iteraciones realizadas: {k}")
