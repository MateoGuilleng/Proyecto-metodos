import numpy as np

print("Metodo iterativo de Gauss-Seidel (tamano n x n)\n")

n = int(input("Ingrese el tamano n de la matriz cuadrada (ejemplo: 2, 3, 4): "))
if n <= 0:
    print("\nError: el tamano de la matriz debe ser un entero positivo.")
    exit()

A = np.zeros((n, n), dtype=float)
b = np.zeros(n, dtype=float)

print("\nIngrese los coeficientes de la matriz A y el termino independiente b:")
for i in range(n):
    print(f"\n--- Ecuacion {i + 1} ---")
    for j in range(n):
        A[i, j] = float(input(f"Coeficiente A[{i + 1},{j + 1}]: "))
    b[i] = float(input(f"Termino independiente b[{i + 1}]: "))

# Verificar que ningun elemento de la diagonal principal sea cero
if np.any(np.diag(A) == 0):
    print("\nError: todos los elementos de la diagonal principal deben ser distintos de cero.")
    exit()

# Calculo del radio espectral de Gauss-Seidel: T_GS = -(D + L)^(-1) * U
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
x = np.zeros(n, dtype=float)
for i in range(n):
    x[i] = float(input(f"Valor inicial de x[{i + 1}]: "))

# Configuracion
tolerancia = 0.0001
max_iteraciones = 100
k = 0

print("\nIteraciones")

while k < max_iteraciones:
    x_anterior = x.copy()

    for i in range(n):
        # Suma usando valores ya actualizados (j < i) y anteriores (j > i)
        suma_anteriores = np.dot(A[i, :i], x[:i])
        suma_siguientes = np.dot(A[i, i + 1:], x_anterior[i + 1:])
        x[i] = (b[i] - suma_anteriores - suma_siguientes) / A[i, i]

    error = np.max(np.abs(x - x_anterior))
    k += 1

    print(f"\nIteracion {k}")
    for i in range(n):
        print(f"x[{i + 1}] = {x[i]:.8f}")
    print(f"Error = {error:.8f}")

    if error < tolerancia:
        print("\nSe alcanzo la tolerancia.")
        break
else:
    print("\nSe alcanzo el maximo de iteraciones sin cumplir la tolerancia.")

print("\nResultado final")
print(f"Radio espectral rho(T_GS) = {radio_espectral_gs:.6f}")
for i in range(n):
    print(f"x[{i + 1}] = {x[i]:.8f}")
print(f"Iteraciones realizadas: {k}")