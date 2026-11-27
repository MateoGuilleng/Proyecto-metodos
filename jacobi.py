import numpy as np

# METODO ITERATIVO DE JACOBI (tamano n x n)

print("Metodo iterativo de jacobi\n")

n = int(input("Ingrese el tamano n de la matriz cuadrada (ejemplo: 2, 3, 4): "))
if n <= 0:
    print("\nError: el tamano de la matriz debe ser un entero positivo.")
    exit()

A = np.zeros((n, n), dtype=float)
b = np.zeros(n, dtype=float)

# Pedir los coeficientes de cada ecuacion
print("\nIngrese los coeficientes de la matriz A y el termino independiente b:")
for i in range(n):
    print(f"\n--- Ecuacion {i + 1} ---")
    for j in range(n):
        A[i, j] = float(input(f"Coeficiente A[{i + 1},{j + 1}]: "))
    b[i] = float(input(f"Termino independiente b[{i + 1}]: "))

# aii diferente a 0
if np.any(np.diag(A) == 0):
    print("\nError: todos los elementos de la diagonal principal deben ser distintos de cero.")
    exit()

# Calculo del radio espectral de Jacobi: T_J = -D^(-1) * (L + U)
D = np.diag(np.diag(A))            # D
L_mas_U = A - D                    # (L + U)
T_J = -np.linalg.inv(D) @ L_mas_U
valores_propios_j = np.linalg.eigvals(T_J)
radio_espectral_j = np.max(np.abs(valores_propios_j))

print(f"\nRadio espectral rho(T_J) = {radio_espectral_j:.6f}")
if radio_espectral_j < 1:
    print("Diagnostico: rho < 1 -> El metodo CONVERGE.")
else:
    print("Diagnostico: rho >= 1 -> El metodo NO CONVERGE.")

print("\nValores iniciales:")
x = np.zeros(n, dtype=float)
for i in range(n):
    x[i] = float(input(f"Valor inicial de x[{i + 1}]: "))

# Configuracion
tolerancia = 0.0001
max_iteraciones = 100
k = 0

print("\nIteraciones:")

while k < max_iteraciones:
    x_anterior = x.copy()
    x_nuevo = np.zeros(n, dtype=float)

    for i in range(n):
        # En Jacobi se usan unicamente valores de la iteracion anterior (x_anterior)
        suma_otros = np.dot(A[i, :i], x_anterior[:i]) + np.dot(A[i, i + 1:], x_anterior[i + 1:])
        x_nuevo[i] = (b[i] - suma_otros) / A[i, i]

    error = np.max(np.abs(x_nuevo - x_anterior))
    x = x_nuevo
    k += 1

    print(f"\nIteracion {k}")
    for i in range(n):
        print(f"x[{i + 1}] = {x[i]:.8f}")
    print(f"Error = {error:.8f}")

    # Detener proceso si el error es suficientemente pequeno
    if error < tolerancia:
        print("\nSe alcanzo la tolerancia.")
        break
else:
    print("\nSe alcanzo el maximo de iteraciones sin cumplir la tolerancia.")

print("\nResultado final:")
print(f"Radio espectral rho(T_J) = {radio_espectral_j:.6f}")
for i in range(n):
    print(f"x[{i + 1}] = {x[i]:.8f}")
print(f"Iteraciones realizadas: {k}")