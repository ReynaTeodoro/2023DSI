import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Parámetros
mu = 6.54  # Media poblacional asumida
sigma = np.sqrt(27.23)  # Desviación estándar poblacional
n = 105  # Tamaño de la muestra
alpha = 0.05  # Nivel de significancia

# Valor crítico de la distribución t para el nivel de significancia
t_critical = t.ppf(1 - alpha, df=n-1)

# Valores del efecto de tamaño
effect_sizes = np.linspace(0, 2, 100)

# Cálculo de la potencia para cada efecto de tamaño
power = []
for effect_size in effect_sizes:
    delta = effect_size * sigma
    standard_error = sigma / np.sqrt(n)
    t_value = (mu - delta - mu) / standard_error
    power.append(1 - t.cdf(t_value, df=n-1))

# Gráfico de la potencia en función del efecto de tamaño
plt.plot(effect_sizes, power)
plt.xlabel("Efecto de tamaño (Diferencia en desviaciones estándar)")
plt.ylabel("Potencia de la prueba")
plt.title("Potencia de la prueba en función del efecto de tamaño")
plt.grid(True)
plt.show()
