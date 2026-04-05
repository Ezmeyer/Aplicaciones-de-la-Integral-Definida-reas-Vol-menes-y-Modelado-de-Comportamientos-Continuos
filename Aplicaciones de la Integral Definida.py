import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import math

# =========================
# 1. Definir la función
# =========================
def f(x):
    return 2*x + 5   # ingresos diarios

# =========================
# 2. Calcular el área
# =========================
area, _ = quad(f, 0, 10)

print("Ingreso total (área bajo la curva):", area)

# =========================
# 3. Calcular volumen
# =========================
def volumen(x):
    return math.pi * (f(x))**2

V, _ = quad(volumen, 0, 10)

print("Volumen de revolución:", V)

# =========================
# 4. Graficar
# =========================
x = np.linspace(0, 10, 100)
y = f(x)

plt.figure()
plt.plot(x, y)
plt.fill_between(x, y, alpha=0.3)

plt.title("Ingresos acumulados de la empresa")
plt.xlabel("Tiempo (días)")
plt.ylabel("Ingresos")

# Guardar imagen para LaTeX
plt.savefig("grafica.png")

plt.show()