
# METODO ITERATIVO DE GAUSS-SEIDEL

# Valores iniciales
x = 1.0
y = 2.0
z = 2.0

# Configuracion
tolerancia = 0.0001
max_iteraciones = 100
k = 0

print("METODO DE GAUSS-SEIDEL")
print("=" * 55)

while k < max_iteraciones:

    # Guardamos los valores de la iteracion anterior
    x_anterior = x
    y_anterior = y
    z_anterior = z

    # Calculamos x con los valores anteriores de y y z
    x = (7 + y_anterior - z_anterior) / 4

    # Usamos inmediatamente el NUEVO valor de x
    y = (21 + 4*x + z_anterior) / 8

    # Usamos el NUEVO valor de x y el NUEVO valor de y
    z = (15 + 2*x - y) / 5

    # Calculamos el error maximo
    error = max(
        abs(x - x_anterior),
        abs(y - y_anterior),
        abs(z - z_anterior)
    )

    k += 1

    print(f"\nIteracion {k}")
    print(f"x = {x:.8f}")
    print(f"y = {y:.8f}")
    print(f"z = {z:.8f}")
    print(f"Error = {error:.8f}")

    if error < tolerancia:
        print("\nSe alcanzo la tolerancia.")
        break

print("\nRESULTADO FINAL")
print(f"x = {x:.8f}")
print(f"y = {y:.8f}")
print(f"z = {z:.8f}")
print(f"Iteraciones realizadas: {k}")
