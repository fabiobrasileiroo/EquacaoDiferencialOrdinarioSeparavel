import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Definindo a equação diferencial
def equation(y, t):
  return 2 * y # Exemplo de equação: y' = 2y

# Denfinindo as condições inicias
t = np.linspace(0, 5, 100) # Vetor de tempos
y0 = 1 # Valor inicial de y

# Resolvendo a equação diferencial
sol = odeint(equation, y0, t)

# Plotando o gráfico da solução
plt.plot(t,sol)
plt.xlabel('Tempo')
plt.ylabel('y')
plt.title('Solução da Equação Diferencial')
plt.grid(True)
plt.show()