# METODO ITERATIVO DE JACOBI

print("Metodo iterativo de jacobi")

print("Ecuacion: a*x + b*y + c*z = d\n")

# Pedir los coeficientes de cada ecuacion
a1 = float(input("Ecuacion 1 - coeficiente de x (a1): "))
b1 = float(input("Ecuacion 1 - coeficiente de y (b1): "))
c1 = float(input("Ecuacion 1 - coeficiente de z (c1): "))
d1 = float(input("Ecuacion 1 - termino independiente (d1): "))

print()
a2 = float(input("Ecuacion 2 - coeficiente de x (a2): "))
b2 = float(input("Ecuacion 2 - coeficiente de y (b2): "))
c2 = float(input("Ecuacion 2 - coeficiente de z (c2): "))
d2 = float(input("Ecuacion 2 - termino independiente (d2): "))

print()
a3 = float(input("Ecuacion 3 - coeficiente de x (a3): "))
b3 = float(input("Ecuacion 3 - coeficiente de y (b3): "))
c3 = float(input("Ecuacion 3 - coeficiente de z (c3): "))
d3 = float(input("Ecuacion 3 - termino independiente (d3): "))

# aii diferente a 0 
if a1 == 0 or b2 == 0 or c3 == 0:
    print("\n Error: los coeficientes en la diagonal (a1, b2, c3) deben ser distintos de cero.")
    exit()

print("\nValores iniciales:")
x = float(input("Valor inicial de x: "))
y = float(input("Valor inicial de y: "))
z = float(input("Valor inicial de z: "))

# Configuracion
tolerancia = 0.0001
max_iteraciones = 100
k = 0

print("Iteraciones: ")


while k < max_iteraciones:

    x_anterior = x
    y_anterior = y
    z_anterior = z


    x_nuevo = (d1 - b1 * y_anterior - c1 * z_anterior) / a1
    y_nuevo = (d2 - a2 * x_anterior - c2 * z_anterior) / b2
    z_nuevo = (d3 - a3 * x_anterior - b3 * y_anterior) / c3

    error = max(
        abs(x_nuevo - x_anterior),
        abs(y_nuevo - y_anterior),
        abs(z_nuevo - z_anterior)
    )

    x = x_nuevo
    y = y_nuevo
    z = z_nuevo

    k += 1

    print(f"\n Iteracion {k}")
    print(f"x = {x:.8f}")
    print(f"y = {y:.8f}")
    print(f"z = {z:.8f}")
    print(f"Error = {error:.8f}")

    # Detener proceso si el error es suficientemente pequeño
    if error < tolerancia:
        print("\nSe alcanzo la tolerancia.")
        break
else:
    print("\n Se alcanzo el maximo de iteraciones sin cumplir la tolerancia.")

print("\n Resultado final: ")
print(f"x = {x:.8f}")
print(f"y = {y:.8f}")
print(f"z = {z:.8f}")
print(f"Iteraciones realizadas: {k}")