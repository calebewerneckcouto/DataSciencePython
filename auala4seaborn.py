import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
base2 = pd.read_csv('train.csv')

# Filtra apenas colunas numéricas
base2_numeric = base2.select_dtypes(include=['number'])

# Substitui valores NaN na coluna 'Age' para evitar problemas
base2['Age'].fillna(base2['Age'].median(), inplace=True)

# Plota um gráfico de barras com a média das idades para cada valor de 'Survived'
plt.figure(figsize=(8, 6))
sns.barplot(x=base2['Survived'], y=base2['Age'])
plt.xlabel('Sobreviveu (0 = Não, 1 = Sim)')
plt.ylabel('Idade Média')
plt.title('Idade Média dos Passageiros por Sobrevivência')
plt.show()

# Calcula a matriz de correlação
corr_matrix = base2_numeric.corr()

# Plota o heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor da Correlação')
plt.show()
