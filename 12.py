import numpy as np
import matplotlib.pyplot as plt

# Dados do problema
T_amb = 25  # Temperatura ambiente (°C)
T_0 = 92    # Temperatura inicial da água (°C)
t = 60      # Tempo (segundos)

# Calcular a constante de resfriamento (k)
k = (-1 / t) * np.log((T_amb - T_0) / (T_amb - T_0))

# Função para calcular a temperatura da água em um determinado tempo t
def temperatura_agua(t):
    return T_amb + (T_0 - T_amb) * np.exp(-k * t)

# Array de tempo de 0 a 60 segundos
tempo = np.arange(0, t+1, 1)

# Calcular a temperatura da água ao longo do tempo
temperatura = temperatura_agua(tempo)

# Plotar o gráfico
plt.plot(tempo, temperatura, label='Temperatura da Água')
plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.title('Resfriamento da Água')
plt.axhline(y=T_amb, color='r', linestyle='--', label='Temperatura Ambiente')
plt.legend()
plt.grid(True)
plt.show()

# Calcular a temperatura da água após 1 minuto (60 segundos)
tempo_1_minuto = 60
temperatura_1_minuto = temperatura_agua(tempo_1_minuto)
print("Temperatura da água após 1 minuto:", temperatura_1_minuto, "°C")
