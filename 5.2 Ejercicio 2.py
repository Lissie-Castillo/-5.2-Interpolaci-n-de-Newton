import numpy as np
import matplotlib.pyplot as plt

# Datos experimentales
T_points = np.array([200, 250, 300, 350, 400])  # Temperatura en °C
efficiency_points = np.array([30, 35, 40, 46, 53])  # Eficiencia en %

# Función para calcular las diferencias divididas
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

# Estimación de eficiencia a T = 275 °C
predicted_efficiency = newton_interpolation(275, T_points, efficiency_points)
print(f"La eficiencia estimada para T = 275 °C es: {predicted_efficiency:.2f} %")

# Puntos para graficar la interpolación
T_values = np.linspace(min(T_points), max(T_points), 100)
efficiency_values = [newton_interpolation(T, T_points, efficiency_points) for T in T_values]

# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(T_values, efficiency_values, label="Interpolación de Newton", color="blue")
plt.scatter(T_points, efficiency_points, color="red", label="Datos experimentales")
plt.scatter(275, predicted_efficiency, color="green", label="Estimación para 275 °C", zorder=5)
plt.xlabel("Temperatura (°C)")
plt.ylabel("Eficiencia (%)")
plt.title("Interpolación de Newton de la Eficiencia del Motor Térmico")
plt.legend()
plt.grid(True)
plt.show()