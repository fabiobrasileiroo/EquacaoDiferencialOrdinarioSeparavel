import numpy as np
import matplotlib.pyplot as plt

# Constantes
T0 = 92  # temperatura inicial da água
Ts = 25  # temperatura da sala
k = np.log((T0 - Ts) / (85 - Ts))  # constante de proporcionalidade

# Função para calcular a temperatura da água no tempo t
def T(t):
    return Ts + (T0 - Ts) * np.exp(-k * t)

# Função para calcular o tempo necessário para a água atingir uma determinada temperatura
def time_to_reach_temperature(T_target):
    return -np.log((T_target - Ts) / (T0 - Ts)) / k

# Calcular a temperatura da água após 1 minuto
T_after_1_minute = T(1)

# Calcular o tempo necessário para a água atingir 60 graus
time_to_60_degrees = time_to_reach_temperature(60)

# Gerar dados para o gráfico
t = np.linspace(0, 10, 100)  # tempo de 0 a 10 minutos
T_t = T(t)  # temperatura da água em cada tempo t

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(t, T_t, label='Temperatura da água')
plt.scatter([1, time_to_60_degrees], [T_after_1_minute, 60], color='red')  # pontos para os tempos específicos
plt.title('Temperatura da água ao longo do tempo')
plt.xlabel('Tempo (minutos)')
plt.ylabel('Temperatura (°C)')
plt.legend()
plt.grid(True)
plt.show()
