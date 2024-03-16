import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definindo a nova equação diferencial
def equation(y, t):
    return -0.5 * y + 1 # Exemplo de equação: y' = -0.5y + 1

# Definindo as condições iniciais
t = np.linspace(0, 10, 100) # Vetor de tempos
y0 = 0 # Valor inicial de y

# Resolvendo a equação diferencial
sol = odeint(equation, y0, t)

# Plotando o gráfico da solução
plt.plot(t, sol)
plt.xlabel('Tempo')
plt.ylabel('y')
plt.title('Solução da Nova Equação Diferencial')
plt.grid(True)
plt.show()
