# import numpy as np
# import matplotlib.pyplot as plt

# # Parâmetros
# t = np.linspace(0, 10, 100)  # Vetor de tempos
# y0 = 25.0  # Temperatura inicial
# k = 0.1  # Taxa de resfriamento

# # Solução analítica
# def analytic_solution(t, y0, k):
#     return y0 * np.exp(-k * t)

# # Solução numérica (resultados anteriores)
# def numeric_solution(t, y0, k):
#     return 25 * np.exp(-0.1 * t)

# # Plotando as soluções
# plt.plot(t, analytic_solution(t, y0, k), label='Solução Analítica')
# plt.plot(t, numeric_solution(t, y0, k), 'r--', label='Solução Numérica')
# plt.xlabel('Tempo')
# plt.ylabel('Temperatura')
# plt.title('Comparação entre Solução Analítica e Numérica')
# plt.grid(True)
# plt.legend()
# plt.show()

# equação diferencial que pode ser usada 
# para modelar problemas climáticos. Vamos considerar a seguinte equação diferencial:
# dydt=−ky
# dtdy​=−ky

# Nesta equação, yy representa a temperatura de uma região, tt é
# o tempo e kk é uma constante que representa a taxa de resfriamento.

# Vamos implementar isso em Python usando odeint:
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definindo a equação diferencial
def climate_equation(y, t, k):
    return -k * y # equação diferencial dy/dt=−ky ou dy*dt = -ky

# Definindo as condições iniciais e parâmetros
t = np.linspace(0, 10, 100)  # Vetor de tempos
y0 = 25.0  # Temperatura inicial
k = 0.1  # Taxa de resfriamento

# Resolvendo a equação diferencial
sol = odeint(climate_equation, y0, t, args=(k,))

# Plotando o gráfico da solução
plt.plot(t, sol)
plt.xlabel('Tempo')
plt.ylabel('Temperatura')
plt.title('Modelo Simples de Problema Climático')
plt.grid(True)
plt.show()

