import numpy as np

print("Metodo iterativo de Gauss-Seidel")

print("Ecuacion: a*x + b*y + c*z = d\n")

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

if a1 == 0 or b2 == 0 or c3 == 0:
    print("\nError: los coeficientes en la diagonal (a1, b2, c3) deben ser distintos de cero.")
    exit()

# Calculo del radio espectral de Gauss-Seidel: T_GS = -(D + L)^(-1) * U
A = np.array([
    [a1, b1, c1],
    [a2, b2, c2],
    [a3, b3, c3]
], dtype=float)

D_mas_L = np.tril(A)               # (D + L)
U = np.triu(A, k=1)                # (U)
T_GS = -np.linalg.inv(D_mas_L) @ U
valores_propios_gs = np.linalg.eigvals(T_GS)
radio_espectral_gs = np.max(np.abs(valores_propios_gs))

print(f"\nRadio espectral rho(T_GS) = {radio_espectral_gs:.6f}")
if radio_espectral_gs < 1:
    print("Diagnostico: rho < 1 -> El metodo CONVERGE.")
else:
    print("Diagnostico: rho >= 1 -> El metodo NO CONVERGE.")

# Pedir valores iniciales
print("\nValores iniciales:")
x = float(input("Valor inicial de x: "))
y = float(input("Valor inicial de y: "))
z = float(input("Valor inicial de z: "))

# Configuracion
tolerancia = 0.0001
max_iteraciones = 100
k = 0

print("\n Iteraciones")

while k < max_iteraciones:

    # Guardamos los valores de la iteracion anterior
    x_anterior = x
    y_anterior = y
    z_anterior = z

    # Despejamos
    x = (d1 - b1 * y_anterior - c1 * z_anterior) / a1

    # Usamos nuevo valor de "x"
    y = (d2 - a2 * x - c2 * z_anterior) / b2

    # Usamos nuevo valor de "x" y "y"
    z = (d3 - a3 * x - b3 * y) / c3

    # Calculamos el error maximo
    error = max(
        abs(x - x_anterior),
        abs(y - y_anterior),
        abs(z - z_anterior)
    )

    k += 1

    print(f"\n Iteracion {k}")
    print(f"x = {x:.8f}")
    print(f"y = {y:.8f}")
    print(f"z = {z:.8f}")
    print(f"Error = {error:.8f}")

    if error < tolerancia:
        print("\n Se alcanzo la tolerancia.")
        break
else:
    print("\nSe alcanzo el maximo de iteraciones sin cumplir la tolerancia.")

print("\n Resultado final")
print(f"Radio espectral rho(T_GS) = {radio_espectral_gs:.6f}")
print(f"x = {x:.8f}")
print(f"y = {y:.8f}")
print(f"z = {z:.8f}")
print(f"Iteraciones realizadas: {k}")