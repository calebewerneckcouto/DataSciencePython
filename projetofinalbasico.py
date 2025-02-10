import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random

# Carregar os dados
df = pd.read_csv(r'train.csv')

# Exibir as primeiras linhas do DataFrame
print(df.head())

# Criar listas para variáveis qualitativas e quantitativas
quali = []
quanti = []

for i in df.dtypes.index:
    if df.dtypes[i] == 'object':
        quali.append(i)
    else:
        quanti.append(i)

# Criar DataFrame apenas com variáveis quantitativas
df_quanti = df[quanti]

# Estatística Descritiva
print("Estatística Descritiva:\n", df_quanti.describe())

# Calculando a Mediana (que não está no describe)
print("Mediana:\n", df.median(numeric_only=True))

# Criando o df_quali
df_quali = df[quali]

# Fazendo a tabela de frequência para a variável 'Sex'
valores = df_quali.groupby('Sex').Name.count()
print(valores)

# Fazendo todas as tabelas de frequência
for i in df_quali.columns:
    if i != 'Name':
        print('----------------------')
        print('Variável: ', i)
        print(df_quali.groupby(i).Name.count())
        print('----------------------')

# Contando valores nulos
nulos = pd.DataFrame({'Variável': df.columns})
nulos['Quantidade'] = df.isna().sum().values
nulos['Porcentagem'] = (df.isna().sum() / df.shape[0]) * 100
print(nulos)

# Removendo linhas nulas da variável 'Embarked'
df2 = df.dropna(subset=['Embarked'])

# Preenchendo a variável 'Age' com a média
df3 = df2.copy()
df3['Age'] = df2['Age'].fillna(df2['Age'].mean())

# Preenchendo a variável 'Cabin' com a moda
df4 = df3.copy()
moda = df4['Cabin'].mode().values
df4['Cabin'] = df4['Cabin'].fillna(random.choice(moda))

# Criando o Boxplot
fig, axs = plt.subplots(2, 3, figsize=(20, 10))

axs[0, 0].set_title('Survived')
axs[0, 0].boxplot(df4['Survived'].dropna())

axs[0, 1].set_title('Pclass')
axs[0, 1].boxplot(df4['Pclass'].dropna())

axs[0, 2].set_title('Age')
axs[0, 2].boxplot(df4['Age'].dropna())

axs[1, 0].set_title('SibSp')
axs[1, 0].boxplot(df4['SibSp'].dropna())

axs[1, 1].set_title('Parch')
axs[1, 1].boxplot(df4['Parch'].dropna())

axs[1, 2].set_title('Fare')
axs[1, 2].boxplot(df4['Fare'].dropna())



# Exibir os gráficos
plt.show()

# Calculo dos Outliers

# Todos os pontos que estão fora do limite superior e inferior da amostra

# Limite superior = Q3 + 1,5 * DistanciaInterquartil
# Limite inferior = Q1 - 1,5 * DistanciaInterquartil

# Distância Interquartil = Valor do 3º Quartil - Valor do 1º Quartil (Q3 - Q1)


# Fazendo este cálculo para estas o Dataframe todo (apenas o quantitativo)

df4_quanti = df4[quanti]
colunas = df4_quanti.columns
outliers = []

for i in df4_quanti.columns:
    
    q3 = np.quantile(df4_quanti[i], 0.75)
    q1 = np.quantile(df4_quanti[i], 0.25)
    dist = q3 - q1 
    lim_inf = q1 - 1.5*dist
    lim_sup = q3 + 1.5*dist
    
    print('--------------')
    print(i)
    print(dist)
    print(lim_inf)
    print(lim_sup)
    print('-------------')

    outlier = 0

    for j in df4_quanti.index:
        if df4_quanti[i][j] < lim_inf:
            outlier = outlier + 1
        elif df4_quanti[i][j] > lim_sup:
            outlier= outlier + 1
        else: 
            pass
        
    outliers.append(outlier)
    
df_outlier = pd.DataFrame()
df_outlier['Variável'] = colunas
df_outlier['Outliers'] = outliers
df_outlier['Porcentagem'] = (outliers/df4_quanti.PassengerId.count()) * 100

print(df_outlier)

sns.countplot(x='Survived', data=df4);



porsexo=df4.groupby(['Survived','Sex'])['Survived'].count() 
print(porsexo)

sns.catplot(x='Sex', col='Survived', kind='count', data=df4);
sns.catplot(x='Pclass', y='Survived', kind='point', data=df4);
sns.catplot(x='Pclass', y='Survived', hue='Sex', kind='point', data=df4)

# Exibir os gráficos
plt.show()

# Calculo dos Outliers

# Todos os pontos que estão fora do limite superior e inferior da amostra

# Limite superior = Q3 + 1,5 * DistanciaInterquartil
# Limite inferior = Q1 - 1,5 * DistanciaInterquartil

# Distância Interquartil = Valor do 3º Quartil - Valor do 1º Quartil (Q3 - Q1)


# Fazendo este cálculo para estas o Dataframe todo (apenas o quantitativo)

df4_quanti = df4[quanti]
colunas = df4_quanti.columns
outliers = []

for i in df4_quanti.columns:
    
    q3 = np.quantile(df4_quanti[i], 0.75)
    q1 = np.quantile(df4_quanti[i], 0.25)
    dist = q3 - q1 
    lim_inf = q1 - 1.5*dist
    lim_sup = q3 + 1.5*dist
    
    print('--------------')
    print(i)
    print(dist)
    print(lim_inf)
    print(lim_sup)
    print('-------------')

    outlier = 0

    for j in df4_quanti.index:
        if df4_quanti[i][j] < lim_inf:
            outlier = outlier + 1
        elif df4_quanti[i][j] > lim_sup:
            outlier= outlier + 1
        else: 
            pass
        
    outliers.append(outlier)
    
df_outlier = pd.DataFrame()
df_outlier['Variável'] = colunas
df_outlier['Outliers'] = outliers
df_outlier['Porcentagem'] = (outliers/df4_quanti.PassengerId.count()) * 100


sns.catplot(x='Survived', col='Embarked', kind='count', data=df4);
sns.barplot(x='Survived', y='Age', data=df4, estimator=np.mean)

# Filtra apenas colunas numéricas
base2_numeric = df.select_dtypes(include=['number'])
# Calcula a matriz de correlação
corr_matrix = base2_numeric.corr()
# Plota o heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor da Correlação')
plt.show()
