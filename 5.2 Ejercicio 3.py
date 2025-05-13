import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales de velocidad (V) y coeficiente de arrastre (Cd)
V_points = np.array([10, 20, 30, 40, 50, 60])  # Velocidad en m/s
Cd_points = np.array([0.32, 0.30, 0.28, 0.27, 0.26, 0.25])  # Coeficiente de arrastre

# Función para calcular diferencias divididas
def divided_differences(x, y):
    n = len(y)
    coef = np.copy(y).astype(float)
    for j in range(1, n):
        coef[j:n] = (coef[j:n] - coef[j - 1:n - 1]) / (x[j:n] - x[0:n - j])
    return coef

# Evaluación del polinomio de Newton
def newton_interpolation(x_val, x_data, y_data):
    coef = divided_differences(x_data, y_data)
    n = len(coef)
    result = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x_val - x_data[j])
        result += term
    return result

# Estimar el coeficiente de arrastre a V = 35 m/s
V_est = 35
Cd_est = newton_interpolation(V_est, V_points, Cd_points)
print(f"El coeficiente de arrastre estimado para V = 35 m/s es: {Cd_est:.4f}")

# Generar puntos para graficar la interpolación
V_values = np.linspace(min(V_points), max(V_points), 100)
Cd_values = [newton_interpolation(V, V_points, Cd_points) for V in V_values]

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(V_values, Cd_values, label="Interpolación de Newton", color="blue")
plt.scatter(V_points, Cd_points, color="red", label="Datos experimentales")
plt.scatter(V_est, Cd_est, color="green", label="Estimación para 35 m/s", zorder=5)
plt.xlabel("Velocidad del aire (m/s)")
plt.ylabel("Coeficiente de arrastre (Cd)")
plt.title("Interpolación de Newton del Coeficiente de Arrastre")
plt.legend()
plt.grid(True)
plt.show()