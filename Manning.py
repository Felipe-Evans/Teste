import numpy as np
import matplotlib.pyplot as plt

# Gerando valores para r
r = np.linspace(-5, 5, 5000)

# Função para o poço duplo
def Poço_duplo(r):
    poço = np.zeros_like(r)
    
    # Primeira parte do poço
    poço[(r >= -1.5) & (r < 0)] = -50
    
    # Segunda parte do poço
    poço[(r > 0) & (r <= 1.5)] = -50
    
    # Barreira central
    poço[(r >= -0.5) & (r <= 0.5)] = -40
    
    return poço

# Constantes
k = 78.95
rho = 0.2516
beta = 27.7
D = 530

# Definindo a função do potencial Manning
def V(r):
    sech_quadrado = (2 / (np.exp(r / (2 * rho)) + np.exp(-r / (2 * rho))))**2
    termo1 = - (beta / 2) * (beta / 2 + 1 / 2) * sech_quadrado
    termo2 = - D * (sech_quadrado - sech_quadrado**2)
    return (1 / (5)) * (termo1 + termo2)



# Calculando os potenciais
V_Pd = Poço_duplo(r)
V_Manning = V(r)

# Plotando os dois potenciais
plt.figure(figsize=(10, 8))
plt.plot(r, V_Pd, label="Poço Duplo", linestyle='--', color='blue')
plt.plot(r, V_Manning, label="Manning", linestyle='-', color='red')
ticks = np.linspace(-5, 5, 21)
plt.xticks(ticks)
plt.title("Comparação entre Poço Duplo e Potencial Manning")
plt.xlabel("Posição (r)")
plt.ylabel("Energia (V)")
plt.grid(True)
plt.legend()
plt.show()
