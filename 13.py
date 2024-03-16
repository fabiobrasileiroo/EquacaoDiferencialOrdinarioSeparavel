import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definindo a equação diferencial
def climate_equation(y, t, k):
    """
    Função que define a equação diferencial do modelo climático.

    Argumentos:
        y: Temperatura da água em um instante específico.
        t: Tempo.
        k: Taxa de resfriamento.

    Retorno:
        A derivada da temperatura em relação ao tempo (dy/dt).
    """
    return -k * (y - 25)

# Definindo as condições iniciais e parâmetros
t = np.linspace(0, 1, 1000)  # Vetor de tempos com 1000 pontos entre 0 e 1 minuto
y0 = 92.0  # Temperatura inicial da água (92°C)
T_a = 25.0  # Temperatura ambiente (25°C)
delta_T = y0 - T_a  # Diferença de temperatura inicial
k = -np.log((y0 - T_a) / delta_T)  # Taxa de resfriamento calculada com base na temperatura ambiente

# Resolvendo a equação diferencial
sol = odeint(climate_equation, y0, t, args=(k,))

# Plotando o gráfico da solução
plt.plot(t, sol, label="Temperatura da Água")
plt.xlabel('Tempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.title('Modelo Simples de Problema Climático')
plt.grid(True)

# Adicionando linha para destacar a temperatura inicial
plt.axhline(y=y0, color='r', linestyle='dashed', label='Temperatura Inicial')
plt.legend()

# Mostrando o gráfico
plt.show()

# Calculando o tempo para atingir a temperatura de 60°C
tempo_60C = t[np.where(sol <= 60)[0][0]]

# Imprimindo os resultados
print(f"Temperatura da água após 1 minuto: {sol[-1][0]:.2f}°C")
print(f"Tempo para atingir 60°C: {tempo_60C:.2f} minutos")
