import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Carregar os dados
base = pd.read_csv('train.csv')

# Criar figura para múltiplos gráficos
plt.figure(figsize=(15, 10))

# Gráfico de linha (idade dos passageiros)
plt.subplot(2, 2, 1)
plt.plot(base.Age)
plt.title("Idade dos passageiros")

# Gráfico de barras (média de idade por sobrevivência)
plt.subplot(2, 2, 2)
plt.bar(['Não sobreviveu', 'Sobreviveu'], [base[base.Survived == 0].Age.mean(), base[base.Survived == 1].Age.mean()])
plt.title("Média de Idade por Sobrevivência")

# Gráfico de dispersão (idade x sobrevivência)
plt.subplot(2, 2, 3)
plt.scatter(base.Survived, base.Age, alpha=0.5, color='red')
plt.title("Dispersão: Sobrevivência x Idade")

# Gráfico de barras horizontais
plt.subplot(2, 2, 4)
plt.barh(['Não sobreviveu', 'Sobreviveu'], [base[base.Survived == 0].Age.mean(), base[base.Survived == 1].Age.mean()], color=['blue', 'orange'])
plt.title("Média de Idade por Sobrevivência (Horizontal)")

plt.tight_layout()
plt.show()

# Removendo valores nulos antes do histograma
base2 = base.dropna(axis=0, subset=['Age'])

# Criar múltiplos histogramas
plt.figure(figsize=(20, 8))
plt.hist(base2.Age, bins=30, color='green', edgecolor='black', alpha=0.7)
plt.title('Histograma de Idade dos Passageiros')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

# Histograma comparativo por sobrevivência
plt.figure(figsize=(20, 8))
plt.hist(base2[base2.Survived == 0].Age, color='red', label='Não Sobreviveu', alpha=0.5, bins=30, edgecolor='black')
plt.hist(base2[base2.Survived == 1].Age, color='blue', label='Sobreviveu', alpha=0.5, bins=30, edgecolor='black')
plt.title('Histograma de Idade dos Passageiros por Sobrevivência')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.legend(loc='upper right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.savefig('gráficoidade.png')
plt.show()
