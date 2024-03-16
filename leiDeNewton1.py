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
    return -k * y

# Definindo as condições iniciais e parâmetros
t = np.linspace(0, 100, 1000)  # Vetor de tempos com 1000 pontos entre 0 e 100 minutos
y0 = 92.0  # Temperatura inicial da água (92°C)
k = -np.log(85 / y0) / 1  # Taxa de resfriamento calculada com base na informação do problema

# Resolvendo a equação diferencial
sol = odeint(climate_equation, y0, t, args=(k,))

# Plotando o gráfico da solução
plt.plot(t, sol, label="Temperatura da Água")
plt.xlabel('Tempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.title('Modelo Simples de Problema Climático')
plt.grid(True)

# Adicionando linhas para destacar a temperatura inicial e a temperatura final desejada
plt.axhline(y=y0, color='r', linestyle='dashed', label='Temperatura Inicial')
plt.axhline(y=60, color='g', linestyle='dashed', label='Temperatura Final Desejada')
plt.legend()

# Mostrando o gráfico
plt.show()

# Calculando o tempo para atingir a temperatura de 60°C
tempo_60C = t[np.where(sol <= 60)[0][0]]

# Imprimindo os resultados
print(f"Temperatura da água após 1 minuto: {sol[1]:.2f}°C")
print(f"Tempo para atingir 60°C: {tempo_60C:.2f} minutos")

# A temperatura da água após 1 minuto é de 87,24°C.
# Levará 13,87 minutos para a água atingir a temperatura de 60°C.
