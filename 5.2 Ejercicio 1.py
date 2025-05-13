import numpy as np
import matplotlib.pyplot as plt

# Definición de los puntos de interpolación
F_points = np.array([50, 100, 150, 200])  # Carga en Newtons
epsilon_points = np.array([0.12, 0.35, 0.65, 1.05])  # Deformación en mm

# Función de interpolación de Newton
def newton_interpolation(x, F_points, epsilon_points):
    n = len(F_points)
    coeffs = np.zeros(n)
    coeffs[0] = epsilon_points[0]
    
    for i in range(1, n):
        coeffs[i] = epsilon_points[i]
        for j in range(i - 1, -1, -1):
            coeffs[j] = (coeffs[j + 1] - coeffs[j]) / (F_points[i] - F_points[j])
    
    result = coeffs[0]
    for i in range(1, n):
        term = coeffs[i]
        for j in range(i):
            term *= (x - F_points[j])
        result += term
    return result

# Estimación de la deformación para una carga de 125 N
estimated_deformation = newton_interpolation(125, F_points, epsilon_points)
print(f"La deformación estimada para una carga de 125 N es: {estimated_deformation:.2f} mm")

# Puntos para graficar la interpolación
x_values = np.linspace(min(F_points), max(F_points), 100)
y_values = [newton_interpolation(x, F_points, epsilon_points) for x in x_values]

# Graficar los puntos y la interpolación
plt.figure(figsize=(8, 5))
plt.plot(x_values, y_values, label="Interpolación de Newton", color="blue")
plt.scatter(F_points, epsilon_points, color="red", label="Puntos dados")
plt.xlabel("Carga (N)")
plt.ylabel("Deformación (mm)")
plt.title("Interpolación de Newton")
plt.legend()
plt.grid(True)
plt.savefig("newton_interpolacion.png")
plt.show()