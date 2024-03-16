plt.xlabel('Tempo (s)')
plt.ylabel('Temperatura (°C)')
plt.title('Resfriamento da Água')
plt.axhline(y=T_amb, color='r', linestyle='--', label='Temperatura Ambiente')
plt.legend()
plt.grid(True)
plt.show()

